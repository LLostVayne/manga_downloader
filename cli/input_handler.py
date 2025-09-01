from cli.output_handler import OutputHandler
from models.chapter import Chapter
from models.manga import Manga


class InputHandler:


    def get_manga_name(self) -> str:
        manga: str = input("Which manga would you like to search? ")

        return manga


    def get_manga_selection(self, mangas: list[Manga], show_columns: bool = True) -> int:
        if show_columns:
            OutputHandler.show_columns(mangas)
        selection: int =  int(input("Select manga: "))

        return selection
    

    def download_all_chapters(self) -> bool:
        download_all: str = input("Download all chapters?[y/n]")
        
        return download_all == "y"


    def download_latest_chapter(self) -> bool:
        download_latest: str = input("Download latest chapter?[y/n]")

        return download_latest == "y"


    def get_chapter_range(self, chapters: list[Chapter]) -> str:
        # OutputHandler.show_columns(chapters, True)
        OutputHandler.show_columns(chapters)
        chapter_range: str = input("Input number range of chapter(s) you want to download\n1: | :2 | 1:4 | 4 | (Empty for skip) \n?> ")
       
        return chapter_range


    def get_chapter_picks(self, chapters: list[Chapter]) -> str:
        # OutputHandler.show_columns(chapters)
        chapter_picks: str = input("Input number picks of chapter(s) you want to download: (1,6,23,90 or Empty for skip) \n?>")

        return chapter_picks


    def get_output_dir(self) -> str:
        output_dir: str = input("Enter output directory(Empty for default): ")
        
        return output_dir
    

    def get_verbose(self) -> bool:
        verbose_option: str = input("Show verbose output?[y/n]")

        return verbose_option == "y"