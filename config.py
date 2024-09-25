"""_summary_
"""

import os
from pathlib import Path

ENV_PREFIX = "RESOQU_"
CONFIG_FILE_NAME = ".resoqu-settings.json"
CONFIG_FILE_HOME_DIR = Path(os.path.expanduser("~")) / CONFIG_FILE_NAME
CONFIG_FILES = (
    CONFIG_FILE_HOME_DIR,
)
