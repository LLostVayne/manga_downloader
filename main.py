from scraper.manga_scraper import MangaScraper
from cli.user_interface.output_handler import OutputHandler
from cli.user_interface.input_handler import InputHandler
from models.manga import Manga
from models.chapter import Chapter
from utils.args import get_args
from argparse import Namespace
from utils.exceptions import NoResultsError

def main():
    args: Namespace = get_args()
    input: InputHandler = InputHandler(args)
    output: OutputHandler = OutputHandler(args)
    scraper: MangaScraper = MangaScraper(args)
    
    mangaInput: str = input.get_manga_search()
    mangas: list[Manga] = scraper.search_manga(mangaInput)
    
    chapters: list[Chapter] | None = []
    
    try:
        if (not args.abs and len(mangas) > 1): # Not absolute and list the mangas
            output.show_columns(mangas)
            mangaChoice: int = input.get_manga_to_download()
            chapters = scraper.search_chapters(mangaChoice)
        elif (args.abs and len(mangas) > 0): # Loop through list in order to find 1:1 manga title
            for index, manga in enumerate(mangas):
                if (manga.title.lower() == mangaInput.lower()):
                    chapters = scraper.search_chapters(index)
        else: # One manga and/or absolute
            chapters = scraper.search_chapters()
    except NoResultsError as error: 
        print(error)


    output.show_columns(chapters, True)
        

if __name__ == "__main__":
    main()