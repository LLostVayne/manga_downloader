from models.download_options import DownloadOptions
from scraper.manga_scraper import MangaScraper
from cli.input_handler import InputHandler
from models.manga import Manga
from cli.args import get_args
from cli.validate import Validate
from utils.chapter_selector import ChapterSelector
from utils.exceptions import (
    NoResultsError,
    EmptyChapterSelection,
    InvalidChapterSelection,
    InvalidChapterType,
    DownloadError,
)
import sys
from scraper.downloader import Downloader
from utils.folder_manager import FolderManager


def main():
    try:
        dl_options: DownloadOptions = DownloadOptions(get_args())
        scraper: MangaScraper = MangaScraper()
        validate: Validate = Validate(dl_options, InputHandler())

        dl_options.name = validate.validate_name_selection()
        mangas: list[Manga] = scraper.fetch_found_mangas(dl_options.name)
        
        selected_manga: Manga = validate.validate_manga_selection(mangas, dl_options.name)
        
        selected_manga.chapters = scraper.search_chapters(selected_manga)
        dl_options.chapter_selection = validate.validate_chapter_selection(selected_manga.chapters)
        selected_manga.chapters = ChapterSelector.parse_chapters(selected_manga.chapters, dl_options.chapter_selection)
        print(selected_manga.chapters)
        
        dl_options.output_dir = validate.validate_output_dir()
        # fm: FolderManager = FolderManager(dl_options.output_dir)
        # fm.create_folders(selected_manga.title)

        FolderManager.initialize_folders(dl_options.output_dir, selected_manga.title)
        dw: Downloader = Downloader()
        dw.download_chapters(selected_manga.chapters)

    except NoResultsError as e:
        print(e)
        sys.exit(1)
    except EmptyChapterSelection as e:
        print(e)
        sys.exit(1)
    except InvalidChapterSelection as e:
        print(e)
        sys.exit(1)
    except InvalidChapterType as e:
        print(e)
        sys.exit(1)
    except DownloadError as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()