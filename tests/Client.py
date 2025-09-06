from datetime import datetime
from pathlib import Path
from typing import Generator

import pytest
import os
import jwt
from jwt import jwks_client, PyJWKClient
from mass_iq.client.Client import Client
import requests
import logging
logging.basicConfig(level=logging.DEBUG)


from io import BytesIO
import requests
from pathlib import Path
import gzip
from io import BytesIO
import shutil



@pytest.fixture(scope="module")
def library_file()-> Generator[Path, None, None]:

    url = "https://github.com/HUPO-PSI/mzIdentML/raw/refs/heads/master/examples/1_2examples/PeptideShaker_mzid_1_2_example/PeptideShaker_mzid_1_2_example.mzid.gz"

    file_path = Path("PeptideShaker_mzid_1_2_example.mzid")

    # download and decompress directly to disk
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with gzip.open(r.raw, "rb") as gz:
            with open(file_path, "wb") as out_file:
                shutil.copyfileobj(gz, out_file)

    yield file_path


    file_path.unlink()

@pytest.fixture(scope="module")
def client()->Generator[Client,None,None]:

    # The Client object is completely configured through the environment
    client = Client()

    yield client

def test_that_client_object_can_be_created(client: Client) -> None:

    start= datetime.now()
    access_token=client.config.access_token
    end = datetime.now()

    logging.debug(f"Took {end - start} seconds")

    start = datetime.now()
    access_token = client.config.access_token
    end = datetime.now()

    logging.debug(f"Took {end - start} seconds")

    header = jwt.get_unverified_header(access_token)

    jwks_uri = "https://login.microsoftonline.com/f11e977c-a565-424b-b114-70151fe16cd0/discovery/v2.0/keys"

    jwks = PyJWKClient(jwks_uri)

    signing_key = jwks.get_signing_key_from_jwt(client.config.access_token)

    # Decode and validate
    decoded_access_token = jwt.decode(client.config.access_token, algorithms="RS256", options={"verify_signature": False})

    assert decoded_access_token['appid']==os.environ["USER_APP_CLIENT_ID"]



def library_file_upload(library_file: Path, client: Client) -> None:
    client.upload_library_file(library_file, "my/remote/path")
