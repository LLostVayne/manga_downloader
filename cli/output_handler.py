from models.manga import Manga
from models.chapter import Chapter

class OutputHandler:
    
    @staticmethod
    def show_columns(data: list[Manga] | list[Chapter], reverse_index: bool = False) -> None:
        for index, value in enumerate(reversed(data) if reverse_index else data):
            print(f"[{index}] {value.title}")