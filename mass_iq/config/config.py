from typing import Literal, Dict

from pydantic import computed_field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    API_V1_STR: str = "/api/v1"
    DOMAIN: str
    HTTP_SCHEME: Literal["http", "https"] = "https"
    SERVICE_PORT: int

    @computed_field
    @property
    def base_url(self) -> str:
        return f"{self.HTTP_SCHEME}://{self.DOMAIN}:{self.SERVICE_PORT}{self.API_V1_STR}"


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

