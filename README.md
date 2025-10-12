## MassIQ Client package

This python package is a client package for the MassIQ API. The client object is configured exclusively through the environment.
Required environmental variables to configure the API to connect against

    DOMAIN
    SERVICE_PORT

Your authentication credentials are provided by massflows and must be stored in the following environmental variables

    USER_APP_CLIENT_ID
    USER_APP_CLIENT_SECRET


## Dependency Management

This project uses Poetry to manage dependencies and build the python package. In order to use Poetry on Windows
use the installer of Python.org (and not the Windows Store Python Distribution) with the option
"Add Python to PATH" checked. Then install Poetry with Powershell using

(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
 
You can run the tests locally by setting the four required environmental variables and run:


    poetry run pytest tests --log-cli-level=INFO

## Compatability

**All dependencies are managed so that they are consistent with the Google Colaboratory Python environment.**


