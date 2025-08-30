import os
from utils.constants import DEFAULT_MANGA_FOLDER, DEFAULT_ROOT_FOLDER


class FolderManager:
    __default_save_path = os.path.join(os.path.expanduser("~"), DEFAULT_ROOT_FOLDER, DEFAULT_MANGA_FOLDER)

    # def __init__(self, output_dir: str):
    #     self.create_folders(output_dir if output_dir != "" else self.__default_save_path)

    @staticmethod
    def create_folders(name: str):
        try:
            os.makedirs(name)
            os.chdir(name)
        except FileExistsError:
            os.chdir(name)


    @staticmethod
    def initialize_folders(output_dir: str, manga_title: str) -> None:
        try:
            dir: str = os.path.join(output_dir, manga_title) if output_dir != "" else os.path.join(FolderManager.__default_save_path, manga_title)
            FolderManager.create_folders(dir)
        except FileExistsError:
            pass