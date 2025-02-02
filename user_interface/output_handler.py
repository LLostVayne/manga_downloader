from Models.manga import Manga
from Models.chapter import Chapter

class OutputHandler:
    
    
    def __init__(self, args):
        self.args = args
    
    
    # def show_searched_manga(self, mangas: list[Manga]) -> None:
    #     for index, manga in enumerate(mangas):
    #         print(f"[{index}] {manga.title}")
    
    
    # def show_chapters(self, chapters: list[Chapter]) -> None:
    #     for index, chapter in enumerate(chapters):
    #         print(f"[{index}] {chapter.title}")
            
            
    def show_columns(self, data: list[Manga] | list[Chapter]) -> None:
        for index, value in enumerate(data):
            print(f"[{index}] {value.title}")
