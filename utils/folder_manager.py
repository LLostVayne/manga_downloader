import os
from utils.constants import DEFAULT_MANGA_FOLDER, DEFAULT_ROOT_FOLDER


class FolderManager:
    __default_save_path = os.path.join(os.path.expanduser("~"), DEFAULT_ROOT_FOLDER, DEFAULT_MANGA_FOLDER)

    def __init__(self, output_dir: str):
        self.create_folders(output_dir if output_dir != "" else self.__default_save_path)


    def create_folders(self, name: str):
        try:
            os.makedirs(name)
            os.chdir(name)
        except FileExistsError:
            os.chdir(name)
            

    # def initialize_folders(self) -> None:
    #     try:
    #         # dir: str = output_dir if output_dir is not None else self.__default_save_path
    #         self.create_folders(self.__output_dir)
    #         # os.chdir(self.__output_dir)
    #     except FileExistsError:
    #         pass