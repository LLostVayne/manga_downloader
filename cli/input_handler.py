from cli.output_handler import OutputHandler
from models.chapter import Chapter
from models.manga import Manga

class InputHandler:
    
    def __init__(self, args):
        self.__args = args

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
    

    def get_chapter_selection(self, chapters: list[Chapter]) -> str:
        OutputHandler.show_columns(chapters, True)
        chaptersInput: str = input("Input number of chapter(s) you want to download\n1: | :2 | 1:4 | 4 | (Empty for skip) \n?> ")
       
        return chaptersInput