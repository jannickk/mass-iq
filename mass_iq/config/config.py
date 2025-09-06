from typing import Literal, Dict
import requests
from pydantic import computed_field
from pydantic_settings import BaseSettings
import urllib
from tenacity import retry, stop_after_attempt
from cachetools import TTLCache, cachedmethod, cached
import operator

class Settings(BaseSettings):

    API_V1_STR: str = "/api/v1"
    DOMAIN: str
    HTTP_SCHEME: Literal["http", "https"] = "https"
    SERVICE_PORT: int
    # Creating a TTL cache
    # TTLCache per instance
    _cache = TTLCache(maxsize=10, ttl=3500)  # 3500 seconds TTL as the token itself is valid for 3600

    # Cached computed field


    @property
    def base_url(self) -> str:
        return f"{self.HTTP_SCHEME}://{self.DOMAIN}:{self.SERVICE_PORT}{self.API_V1_STR}"


    # Using a decorator to cache function results
    @computed_field()
    @retry(stop=stop_after_attempt(3))
    def access_token(self) -> str:


        if "access_token" in self._cache:
                # If the data is already in the cache, return it directly
            return self._cache["access_token"]
        else:

            post_body = {
                "scope": "https://graph.microsoft.com/.default",
                "client_id": self.USER_APP_CLIENT_ID,
                "client_secret": self.USER_APP_CLIENT_SECRET,
                "grant_type": "client_credentials"
            }

            response = requests.post(
                url=self.OIDC_TOKEN_URL,
                data=urllib.parse.urlencode(post_body),
                headers={'Content-Type': 'application/x-www-form-urlencoded'}
            )

            if response.status_code != 200:

                raise Exception(f"Token request has status code {response.status_code} and response body {response.text}")

            else:

                print("Token request successful")

                self._cache["access_token"] = response.json()["access_token"]
                return self._cache["access_token"]


    @property
    @computed_field(return_type=str)
    def authorization_header(self) -> dict[str, str]:

        return {"Authorization": f"Bearer {self.access_token}"}


    TLS_VERIFY: bool = False
    USER_APP_CLIENT_ID: str
    USER_APP_CLIENT_SECRET: str
    PARALLEL_THREADS_UPLOAD: int = 8

    OIDC_WELL_KNOWN_URL: str = "https://login.microsoftonline.com/f11e977c-a565-424b-b114-70151fe16cd0/v2.0/.well-known/openid-configuration"
    OIDC_TOKEN_URL: str = "https://login.microsoftonline.com/f11e977c-a565-424b-b114-70151fe16cd0/oauth2/v2.0/token"
    OIDC_USERINFO_URL: str = "https://graph.microsoft.com/oidc/userinfo"

    ENDPOINTS : Dict[str, Dict[str, str]] = {
                    "upload": {
                                "libraries": "upload/files/batch/libraries",
                                "sourcefiles": "upload/files/batch/sourcefiles"
                            }
                }

