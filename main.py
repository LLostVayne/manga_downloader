from scraper.manga_scraper import MangaScraper
from user_interface.output_handler import OutputHandler
from user_interface.input_handler import InputHandler
from Models.manga import Manga
from Models.chapter import Chapter
from utils.args import get_args
from argparse import Namespace


def main():
    args: Namespace = get_args()
    input: InputHandler = InputHandler(args)
    output: OutputHandler = OutputHandler(args)
    scraper: MangaScraper = MangaScraper(args)
    
    mangaInput: str = input.get_manga_search()
    mangas: list[Manga] = scraper.search_manga_list(mangaInput)
    
    output.show_columns(mangas)
    
    mangaChoice: int = input.get_manga_to_download()
    chapters: list[Chapter] = scraper.search_manga_chapters(mangaChoice)
    
    output.show_columns(chapters)
        

if __name__ == "__main__":
    main()