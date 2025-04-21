import sys

from scraper.manga_scraper import MangaScraper
from cli.output_handler import OutputHandler
from cli.input_handler import InputHandler
from models.manga import Manga
from models.chapter import Chapter
from cli.args import get_args
from argparse import Namespace
from cli.validate import Validate
from utils.exceptions import NoResultsError


def main():
    try:
        args: Namespace = get_args()
        input_handler: InputHandler = InputHandler(args)
        output: OutputHandler = OutputHandler(args)
        scraper: MangaScraper = MangaScraper(args)
        validate: Validate = Validate(args, input_handler, output)

        manga_name: str = validate.validate_name_selection()
        mangas: list[Manga] = scraper.search_manga(manga_name)

        manga_selection: int = validate.validate_manga_selection(mangas)
        chapters: list[Chapter] | None = scraper.search_chapters(manga_selection)
        output.show_columns(chapters, True)

        validate.validate_chapter_selection()
    except NoResultsError as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()