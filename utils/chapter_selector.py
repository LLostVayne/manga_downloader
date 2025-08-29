from typing import Union
from models.chapter import Chapter
from models.chapter_selection import ChapterSelection
import re
from utils.exceptions import InvalidChapterSelection


class ChapterSelector:

    @staticmethod
    def parse_chapters(chapters: list[Chapter], dl_options_selection: Union[ChapterSelection, str]) -> Union[list[Chapter], Chapter]:
        if dl_options_selection == ChapterSelection.ALL:
            return chapters
        elif dl_options_selection == ChapterSelection.LATEST:
            return chapters[0]
        elif (re.search("^\\d", dl_options_selection) or re.search("\\d$", dl_options_selection)) and dl_options_selection.count(":") == 1:
            return ChapterSelector.__parse_range(chapters, dl_options_selection)
        elif dl_options_selection.count(":") == 0 and dl_options_selection.isnumeric(): # Single chapter e.g. 5
            return chapters[int(dl_options_selection)]
        else:
            raise InvalidChapterSelection("Enter correct chapter selection.")


    @staticmethod
    def __parse_range(chapters: list[Chapter], dl_options_selection: Union[ChapterSelection, str]) -> list[Chapter]:
        split_chapter_selection = dl_options_selection.split(":")
        colon_index = dl_options_selection.find(":")
        chapters_to_download: list[Chapter] = []

        if colon_index == 0: # Colon at the start of the string e.g. :5
            for chapter in chapters[:int(split_chapter_selection[1])]:
                chapters_to_download.append(chapter)
        elif colon_index == len(dl_options_selection) - 1: # Colon at the end of the string e.g. 10:
            for chapter in chapters[int(split_chapter_selection[0]):]:
                chapters_to_download.append(chapter)
        elif len(split_chapter_selection) == 2: # Colon at the middle of the string 2:6
            for chapter in chapters[int(split_chapter_selection[0]):int(split_chapter_selection[1])]:
                chapters_to_download.append(chapter)

        return chapters_to_download