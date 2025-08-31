from requests import Session

from config.config import Settings
import concurrent.futures
from pathlib import Path
import requests
import re
import urllib
from tenacity import retry, stop_after_attempt
from urllib.parse import urljoin

class Client:

    def __init__(self):

        self.__config= Settings()


    def _build_url(self, path: str, parameter: dict = None) -> str:
        if parameter is None:
            return urljoin(self.__config.base_url + "/", path.lstrip("/"))
        else:
            return urljoin(self.__config.base_url + "/", path.lstrip("/"))+"?"+urllib.parse.urlencode(parameter)

    @retry(stop=stop_after_attempt(3))
    def get_access_token(self) -> str:

        post_body = {
            "scope": "https://graph.microsoft.com/.default",
            "client_id": self.__config.USER_APP_CLIENT_ID,
            "client_secret": self.__config.USER_APP_CLIENT_SECRET,
            "grant_type": "client_credentials"
        }

        response = requests.post(
            url=self.__config.OIDC_TOKEN_URL,
            data=urllib.parse.urlencode(post_body),
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )

        if response.status_code != 200:

            raise Exception(f"Token request has status code {response.status_code} and response body {response.text}")

        else:

            return response.json()["access_token"]

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
                    "Authorization": f"Bearer {self.get_access_token()}"
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





