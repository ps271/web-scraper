import os
from dotenv import load_dotenv

load_dotenv(override=False)


class Config:
    APP_NAME = os.environ['APP_NAME']

    APP_INSTANCE_NAME = os.environ['APP_INSTANCE_NAME']

    # Environment
    ENVIRONMENT = os.environ['ENVIRONMENT']

    # Log
    LOG_LEVEL = os.environ['LOG_LEVEL']
    LOG_FILE_INFO = os.environ['LOG_FILE_INFO']
    LOG_FILE_ERROR = os.environ['LOG_FILE_ERROR']