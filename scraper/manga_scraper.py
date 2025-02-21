import requests
from requests import Response
from bs4 import BeautifulSoup, Tag
from models.manga import Manga
from models.chapter import Chapter
from utils.exceptions import NoResultsError

class MangaScraper:

    def __init__(self, args):
        self.args = args
        self.USER_AGENT: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0" 
        self.HEADERS: dict[str, str] = { "User-Agent" : self.USER_AGENT }
        self.url: str = "https://mangakatana.com/?search_by=book_name&search={}"
        self.mangaList: list[Manga] = []
        self.chapterList: list[Chapter] = []

    
    def search_manga(self, title: str) -> list[Manga]:
        """
        Searches MangaKatana for the provide manga title.
        Raises an error if no results were found.
        If the manga title is unique the site will redirect to the manga page immediatly so it grabs the response.url instead of parsing for it.
        
        :param title: Name of the manga.
        :return: Returns a list of manga(s)
        """
        
        soup, response = self.fetch_page(self.url.format(title))
        book_list = soup.find(id = "book_list")
        
        if book_list is not None and "Not found any results" in book_list.text.strip():
            raise NoResultsError("No mangas found.")
        elif isinstance(book_list, Tag): 
            for item in book_list.find_all("div", {"class" : "item"}):
                mangaItem = item.find(class_ = "title").a
                self.mangaList.append(Manga(mangaItem.text, mangaItem.get("href"), None))
        else: 
            self.mangaList.append(Manga(title, response.url, None))
        
        return self.mangaList
    
    
    def search_chapters(self, choice: int = 0) -> list[Chapter]:
        """
        Searches the chapter page for all the chapters.
        Raises an error if not chapters were found.

        :param choice: Input for the user if the search_manga returned a list of mangas if not the manga is unique so default to 0.
        :return: Returns a list of chapters.
        """
        
        soup = self.fetch_page(self.mangaList[choice].url)[0]
        table  = soup.find(class_ = "chapters")

        if isinstance(table, Tag):
            for chapter in table.find_all("div", {"class": "chapter"}):
                self.chapterList.append(Chapter(chapter.text, chapter.a.get("href")))
        else:
            raise NoResultsError("No chapters found.") # Needs to change
            
        return self.chapterList
            
            
            
    def fetch_page(self, url) -> tuple[BeautifulSoup, Response]:
        """
        Fetches url page and returns a tuple of a Soup and Response
        """
        
        r: Response = requests.get(url, headers = self.HEADERS)
        soup: BeautifulSoup = BeautifulSoup(r.text, "html.parser")
        
        return (soup, r)