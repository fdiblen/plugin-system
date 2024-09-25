from typing import List
from git import Repo, rmtree

from .fs_utils import check_file_or_directory_exist, move_file


def checkout_subfolders(
    repo_url: str = 'https://github.com/NLeSC/python-template',
    target_folder: str = "test_repo",
    branch: str = "main",
    sub_folders: List[str] = []
):
    """Clone a repo and checkout subfolders"""

    print(f"* Cloning {repo_url}")
    repo = Repo.init(target_folder)
    origin = repo.create_remote("origin", repo_url)
    origin.fetch()
    git = repo.git()

    for __subfolder in sub_folders:
        print(f"  - Checking out {__subfolder}")
        git.checkout(f"origin/{branch}", "--", __subfolder)
        check_file_or_directory_exist(__subfolder)
        move_file(
            source_path=f"{target_folder}/{__subfolder}",
            target_path="plugins/extra"
        )

    rmtree(f"{target_folder}/.git")
    rmtree(f"{target_folder}")


if __name__ == "__main__":
    checkout_subfolders()
