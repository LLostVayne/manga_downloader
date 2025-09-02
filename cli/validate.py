from typing import Union

from models.enums.information_output import InformationOutput
from models.media.chapter import Chapter
from models.download_options import DownloadOptions
from utils.exceptions import EmptyChapterSelection
from cli.handlers.input_handler import InputHandler
from models.media.manga import Manga
from models.enums.chapter_selection import ChapterSelection

class Validate:
    """The Validate class is used to validate values between the flag and interactive mode of the cli part of the application"""
    
    def __init__(self, dl_options: DownloadOptions, input_handler: InputHandler) -> None:
        self.__dl_options = dl_options
        self.__input: InputHandler = input_handler

    
    def validate_name_selection(self) -> str:
        """
        Validates the manga name for flag '-n, --name' otherwise prompt the user for manga name input.
        :return: User entered manga name.
        """

        return self.__input.get_manga_name() if self.__dl_options.name is None else self.__dl_options.name
    
    
    def validate_manga_selection(self, mangas: list[Manga], selected_manga: str) -> Manga:
        """
        Validates the manga selection by asking the user to select a single manga from the list otherwise
        checks the flag '-abs, --absolute' in order to find 1:1 name but does not prompt user for input.

        :param mangas: List of mangas to validate.
        :param selected_manga: User selected manga.
        :return: The chosen manga to download from.
        """
        
        if len(mangas) == 1: # One manga and/or absolute
            return mangas[0]

        if self.__dl_options.absolute: # Absolute and loop through list in order to find 1:1 manga title
            for index, manga in enumerate(mangas):
                if manga.title.lower() == selected_manga.lower():
                    return mangas[index]
        else: # Not absolute and list the mangas
            return mangas[self.__input.get_manga_selection(mangas)]

 
    def validate_chapter_selection(self, chapters: list[Chapter]) -> Union[ChapterSelection, str]:
        """
        Validates the exclusive chapter selection by going through the validation methods for 'all', 'latest', and 'range'.

        :raise EmptyChapterSelection: If the chapter selection remains empty.
        :param chapters: List of chapters to select for range.
        :return: Union type ChapterSelection or String with the chapter selection range.
        """
        
        if self.__dl_options.chapter_range:
            return self.__dl_options.chapter_range

        if self.__dl_options.all:
            return ChapterSelection.ALL

        if self.__dl_options.latest:
            return ChapterSelection.LATEST

        if self.__dl_options.chapter_pick:
            return self.__dl_options.chapter_pick

        chapter_range: str = self.__input.get_chapter_range(chapters)

        if chapter_range != "":
            return chapter_range

        chapter_picks: str = self.__input.get_chapter_picks(chapters)

        if chapter_picks != "":
            return chapter_picks

        if self.__input.download_latest_chapter():
            return ChapterSelection.LATEST

        if self.__input.download_all_chapters():
            return ChapterSelection.ALL

        raise EmptyChapterSelection("Chapter selection cannot be empty")


    def validate_output_dir(self) -> Union[str, None]:
        """
        Validates the output directory for the downloaded mangas and its chapters, otherwise prompt use for input.

        :return:
        """

        return self.__dl_options.output_dir if self.__dl_options.output_dir is not None else self.__input.get_output_dir()


    def validate_verbose(self) -> bool:
        """
        Validates the verbose option for showcasing more detailed information, otherwise prompt user for input.
        
        :return: boolean value for verbose option.
        """

        return self.__dl_options.verbose if self.__dl_options.verbose else self.__input.get_verbose()


    def validate_information_output(self) -> Union[InformationOutput, None]:
        if self.__dl_options.verbose:
            return InformationOutput.VERBOSE

        if self.__dl_options.progress_bar:
            return InformationOutput.PROGRESS

        verbose: bool = self.__input.get_verbose()

        if verbose:
            return InformationOutput.VERBOSE

        progress_bar: bool = self.__input.get_progress_bar()

        if progress_bar:
            return InformationOutput.PROGRESS

        return None
