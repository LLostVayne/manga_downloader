from models.chapter import Chapter
from models.download_options import DownloadOptions
from utils.exceptions import EmptyChapterSelection
from .input_handler import InputHandler
from models.manga import Manga


class Validate:
    """The Validate class is used to validate values between the flag and interactive mode of the cli part of the application"""
    
    def __init__(self, args, input_handler) -> None:
        self.__args = args
        self.__input: InputHandler = input_handler

    
    def validate_name_selection(self) -> str:
        return self.__input.get_manga_name() if self.__args.name is None else self.__args.name
    
    
    def validate_manga_selection(self, mangas: list[Manga]) -> int:
        if not self.__args.absolute and len(mangas) > 1: # Not absolute and list the mangas
            return self.__input.get_manga_selection(mangas)
        elif self.__args.absolute and len(mangas) > 1: # Absolute and loop through list in order to find 1:1 manga title
            for index, manga in enumerate(mangas):
                if manga.title.lower() == self.__args.name.lower():
                    return index
        else: # One manga and/or absolute
            return 0


    def validate_all_selection(self) -> str:
        if self.__args.all:
            return "all"
        else:
            return "all" if self.__input.download_all_chapters() else ""

    
    def validate_latest_selection(self) -> str:
        if self.__args.latest:
            return "latest"
        else:
            return "latest" if self.__input.download_latest_chapter() else ""


    def validate_range_selection(self, chapters: list[Chapter]) -> str | None:
        return self.__input.get_chapter_selection(chapters) if self.__args.range is None else self.__args.range


    def validate_chapter_selection(self, chapters: list[Chapter], dl_options: DownloadOptions) -> None:
        if not self.__args.latest and not self.__args.all:
            dl_options.chapter_selection = self.validate_range_selection(chapters)

        if dl_options.chapter_selection == "" and not self.__args.all:
            dl_options.chapter_selection = self.validate_latest_selection()

        if dl_options.chapter_selection == "":
            dl_options.chapter_selection = self.validate_all_selection()

        if dl_options.chapter_selection == "":
            raise EmptyChapterSelection("Chapter selection cannot be empty")

