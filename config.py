"""_summary_
"""

import os
from pathlib import Path

ENV_PREFIX = "PYPS_"
CONFIG_FILE_NAME = ".pyps.json"
CONFIG_FILE_HOME_DIR = Path(os.path.expanduser("~")) / CONFIG_FILE_NAME
CONFIG_FILES = (
    CONFIG_FILE_HOME_DIR,
)
