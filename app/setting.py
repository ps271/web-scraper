import os
import pathlib

class Setting:
    # The fill path of this repository

    PROJECT_BASE_DIR = str(pathlib.Path(os.path.abspath(os.path.join(os.getcwd(), __file__))).parent.parent)
    ALLOWED_ENVIRONMENT = {'STAGING', 'PRODUCTION'}