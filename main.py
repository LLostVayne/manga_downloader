from models.download_options import DownloadOptions
from scraper.manga_scraper import MangaScraper
from cli.input_handler import InputHandler
from models.manga import Manga
from models.chapter import Chapter
from cli.args import get_args
from argparse import Namespace
from cli.validate import Validate
from utils.exceptions import NoResultsError, EmptyChapterSelection
import sys


def main():
    
    try:
        args: Namespace = get_args()
        dl_options: DownloadOptions = DownloadOptions()
        input_handler: InputHandler = InputHandler(args)
        scraper: MangaScraper = MangaScraper()
        validate: Validate = Validate(args, input_handler)

        dl_options.name = validate.validate_name_selection()
        mangas: list[Manga] = scraper.search_manga(dl_options.name)
        manga_selection: int = validate.validate_manga_selection(mangas)

        chapters: list[Chapter] = scraper.search_chapters(manga_selection, mangas)
        validate.validate_chapter_selection(chapters, dl_options)


    except NoResultsError as e:
        print(e)
        sys.exit(1)
    except EmptyChapterSelection as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()