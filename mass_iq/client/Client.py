
from mass_iq.config.config import Settings
import concurrent.futures
from pathlib import Path
import requests
import re
import urllib
from tenacity import retry, stop_after_attempt
from urllib.parse import urljoin
import json



class Client:

    def __init__(self):

        self.__config= Settings()

        self.proteomics= ProteomicsClient()

    @property
    def config(self):
        return self.__config


    def _build_url(self, path: str, parameter: dict = None) -> str:

        if parameter is None:

            return urljoin(self.__config.base_url + "/", path.lstrip("/"))

        else:

            return urljoin(self.__config.base_url + "/", path.lstrip("/"))+"?"+urllib.parse.urlencode(parameter)

    def upload_file(self, file: Path, url: str):

        print("Uploading file using the following url: {url}".format(url=url))

        if not file.exists():
            raise Exception(f"file {file.absolute()} does not exist")

        if not file.is_file():
            raise Exception(f"file {file.absolute()} is not a file")

        with open(file, 'rb') as f:

            print(f"Uploading file with absolute path {file.absolute()}\n")

            files = {
                "file": (str(file.absolute()), f)
            }

            response = requests.post(
                url,
                headers={
                    "Authorization": f"Bearer {self.config.access_token}"
                },
                files=files,
                verify=self.__config.TLS_VERIFY,
                stream=True
            )

            if response.status_code == 200:

                print(f"Successfully uploaded file {file.absolute()}\n")

            else:

                print(f"Encountered error uploading file {file.absolute()} with error {response.text}")

                raise Exception(f"Encountered error in library upload")

    def list_files_in_local_directory(self, local_directory: str) -> list[Path]:

        p = Path(local_directory)

        files = p.glob('*')  # a generator to get lists all files recursively

        return [file for file in files if re.match(".*\\.wiff$|.*\\.wiff.scan$", file.name)]

    ############# Resource specific endpoints ####################

    def upload_library_file(self,file: Path, user_defined_path: str):

        url = self._build_url(self.__config.ENDPOINTS["upload"]["libraries"], {"user_defined_path": user_defined_path})

        self.upload_file(file,url)

    def upload_source_file(self,file: Path, user_defined_path: str):

        url = self._build_url(self.__config.ENDPOINTS["upload"]["sourcefiles"], {"user_defined_path": user_defined_path})

        self.upload_file(file,url)

    def upload_batch(self,local_directory: str, user_defined_path: str):

        files = self.list_files_in_local_directory(local_directory)

        print("Found the following files")
        print(f"{files}")

        file_range = list(range(0, len(files), self.__config.PARALLEL_THREADS_UPLOAD))

        file_range.append(len(files))

        for ind in range(len(file_range) - 1):

            with concurrent.futures.ThreadPoolExecutor(max_workers=self.__config.PARALLEL_THREADS_UPLOAD) as executor:

                futures = [executor.submit(self.upload_source_file, file, user_defined_path) for file in files[file_range[ind]:file_range[ind + 1]]]

                concurrent.futures.wait(futures)



class ProteomicsClient:

    def __init__(self):
        pass

    @staticmethod
    def get_isolation_window_for_transition(client:Client,transition, data_reference):

        response = requests.post(f"{client.config.base_url}/data/isolation-windows/by-mz-value",
            data=json.dumps(
                {
                        "mz_target": {
                            "type": "mz-target",
                            "value": transition['precursor_calculated_mz']
                        },
                        "data_reference": data_reference,
                        "schema_version": "v2"
                    }
            ),
            headers=client.config.authorization_header, verify=False
        )

        # Isolation Windows is a list of JSON objects

        isolation_windows = response.json()

        # mz may be in isolation window overlap, so we use the one where the distance of target m/z is maximal to border distance
        # NOTE: For the example of the XICs below, PeakView took the isolation window with lower mz range, for comparability i adabted. To get the best window, make this `max()`

        if len(isolation_windows) > 1:
            # Calculate distance to borders for each window
            get_distance = lambda window, transition: min(
                abs(transition['precursor_calculated_mz'] - window['isolationWindowLowerEnd']),
                abs(transition['precursor_calculated_mz'] - window['isolationWindowUpperEnd'])
            )

            # NOTE: For the example of the XICs below, PeakView took the isolation window with lower mz range, for comparability i adabted. To get the best window, make this `max()`
            best_window = min(isolation_windows, key=lambda window: get_distance(window, transition)) #

            return best_window

        elif len(isolation_windows) == 1:

            return isolation_windows[0]

        else:
            # No isolation window found
            return None