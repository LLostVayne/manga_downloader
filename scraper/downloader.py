from typing import Union
from models.chapter import Chapter
from utils.exceptions import InvalidChapterType
from utils.page_fetcher import fetch_page


class Downloader:

    def download_chapters(chapters: Union[list[Chapter], Chapter]):
        if isinstance(chapters, list):
            # for chapter in chapters:
            soup, response = fetch_page(chapters[0].url)
            imgs = soup.find(id = "imgs")
            total_pages = imgs.find(id="page1").get("data-pages")
        elif isinstance(chapters, Chapter):
            raise NotImplementedError
        else:
            raise InvalidChapterType("Chapters has to be of type list[Chapter] or Chapter")

        


    def __get_total_pages(self):
        raise NotImplementedError
            

