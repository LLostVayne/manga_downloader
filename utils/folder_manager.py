import os

class FolderManager:

    @staticmethod
    def create_folders(title: str):
        try:
            os.mkdir(title)
        except FileExistsError:
            pass
