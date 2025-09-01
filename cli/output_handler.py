from models.media_item import MediaItem


class OutputHandler:

    def __init__(self, verbose: bool, count: bool):
        self.__verbose = verbose
        self.__count = count


    @staticmethod
    def show_columns(data: list[MediaItem]) -> None:
        for index, value in enumerate(data):
            print(f"[{index}] {value.title}")
            

    def info_message(self, message: str):
        print(message)


    def verbose_message(self, message: str):
        if self.__verbose:
            print(message)


    def count_message(self, chapter_count: int):
        if self.__count:
            print(f"Downloaded {chapter_count} chapters in total.")