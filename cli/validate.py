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
        """
        Validates the manga name for flag '-n, --name' otherwise prompt the user for manga name input.
        :return: User entered manga name.
        """

        return self.__input.get_manga_name() if self.__args.name is None else self.__args.name
    
    
    def validate_manga_selection(self, mangas: list[Manga], selected_manga: str) -> Manga:
        """
        Validates the manga selection by asking the user to select a single manga from the list otherwise
        checks the flag '-abs, --absolute' in order to find 1:1 name but does not prompt user for input.

        :param mangas: List of mangas to validate.
        :param selected_manga: User selected manga.
        :return: The chosen manga to download from.
        """
        
        if not self.__args.absolute and len(mangas) > 1: # Not absolute and list the mangas
            return mangas[self.__input.get_manga_selection(mangas)]
        elif self.__args.absolute and len(mangas) > 1: # Absolute and loop through list in order to find 1:1 manga title
            for index, manga in enumerate(mangas):
                if manga.title.lower() == selected_manga.lower():
                    return mangas[index]
        else: # One manga and/or absolute
            return mangas[0]


    def validate_all_selection(self) -> str:
        """
        Validate if the exclusive '-a, --all' flag is set otherwise ask the user to select all chapters.

        :return: String with 'all' or ''
        """
        if self.__args.all:
            return "all"
        else:
            return "all" if self.__input.download_all_chapters() else ""

    
    def validate_latest_selection(self) -> str:
        """
        Validate if the exclusive '-l, --latest' flag is set otherwise ask the user to select latest chapter.

        :return: String with 'latest' or ''
        """
        if self.__args.latest:
            return "latest"
        else:
            return "latest" if self.__input.download_latest_chapter() else ""


    def validate_range_selection(self, chapters: list[Chapter]) -> str:
        """
        Validate if the exclusive '-r, --range' flag is set otherwise ask the user to select range of chapters.

        :param chapters: List of chapters to select from.
        :return: String with the range of the chapters or ''
        """
        return self.__input.get_chapter_selection(chapters) if self.__args.range is None else self.__args.range


    def validate_chapter_selection(self, chapters: list[Chapter], dl_options: DownloadOptions) -> str:
        """
        Validates the exclusive chapter selection by going through the validation methods for 'all', 'latest', and 'range'.

        :raise EmptyChapterSelection: If the chapter selection is empty.
        :return: String with the chapter selection.
        """
        chapter_selection: str = ""

        if not self.__args.latest and not self.__args.all:
            chapter_selection = self.validate_range_selection(chapters)

        # Range is empty
        if chapter_selection == "" and not self.__args.all:
            chapter_selection = self.validate_latest_selection()

        # Range and latest is empty
        if chapter_selection == "":
            chapter_selection = self.validate_all_selection()

        if chapter_selection != "":
            return chapter_selection
        else:
            raise EmptyChapterSelection("Chapter selection cannot be empty")