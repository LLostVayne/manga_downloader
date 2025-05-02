import requests
from requests import Response
from bs4 import BeautifulSoup, Tag
from models.manga import Manga
from models.chapter import Chapter
from utils.exceptions import NoResultsError
from utils.constants import HEADERS

class MangaScraper:
    """The MangaScraper class is used to scrape data for the manga(s) and the chapter(s)."""

    def __init__(self):
        self.__url: str = "https://mangakatana.com/?search_by=book_name&search={}"


    def search_manga(self, title: str) -> list[Manga]:
        """
        Searches MangaKatana for the provide manga title.
        Raises an error if no results were found.
        If the manga title is unique the site will redirect to the manga page immediately so it grabs the response.url instead of parsing for it.

        :param title: Name of the manga.
        :return: Returns a list of manga(s)
        """

        soup, response = self.fetch_page(self.__url.format(title))
        book_list = soup.find(id="book_list")
        mangas: list[Manga] = []
        
        if book_list is not None and "Not found any results" in book_list.text.strip():
            raise NoResultsError("No mangas found.")
        elif isinstance(book_list, Tag):
            for item in book_list.find_all("div", {"class" : "item"}):
                manga_item = item.find(class_ = "title").a # type: ignore
                mangas.append(Manga(manga_item.text, manga_item.get("href"), None)) # type: ignore
        else:
            mangas.append(Manga(title, response.url, None))

        return mangas


    def search_chapters(self, choice: int, mangas: list[Manga]) -> list[Chapter]:
        """
        Searches the chapter page for all the chapters.
        Raises an error if no chapters were found.

        :param choice: Input for the user if the search_manga returned a list of mangas if not the manga is unique so default to 0.
        :param mangas: List of manga(s)
        :return: Returns a list of chapters.
        """
        soup = self.fetch_page(mangas[choice].url)[0]
        table = soup.find(class_="chapters")
        chapters: list[Chapter] = []

        if isinstance(table, Tag):
            for chapter in table.find_all("div", {"class": "chapter"}):
                chapters.append(Chapter(chapter.text, chapter.a.get("href"))) # type: ignore

            return chapters
        else:
            raise NoResultsError("No chapters found.") # Needs to change


    def fetch_page(self, url: str) -> tuple[BeautifulSoup, Response]:
        """
        Fetches url page and returns a tuple of a Soup and Response
        """

        r: Response = requests.get(url, headers=HEADERS)
        r.raise_for_status()
        soup: BeautifulSoup = BeautifulSoup(r.text, "html.parser")

        return soup, r