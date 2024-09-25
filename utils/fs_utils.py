"""_summary_"""

from pathlib import Path
import shutil
import os


def check_file_or_directory_exist(pathname) -> bool:
    """_summary_

    Args:
        pathname (_type_): _description_
    """

    file_or_directory = Path(pathname)

    __check_status = False

    if file_or_directory.exists():
        # if file_or_directory.is_file():
        #     print(f'Filename {pathname} is a file!')
        # else:
        #     print(f'Filename {pathname} is a directory!')
        __check_status = True
    else:
        print(f'    Filename {pathname} does not exists.')

    return __check_status


def move_file(source_path: str, target_path: str):
    """_summary_

    Args:
        source_path (str): _description_
        target_path (str): _description_
    """

    print(f"    Moving: {source_path} --> {target_path}")
    filename = Path(source_path).name

    if os.path.isfile(os.path.join(target_path, filename)):
        print("    File exist. Skipping...")
    else:
        shutil.move(source_path, target_path)
