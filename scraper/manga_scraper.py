import requests
from requests import Response
from bs4 import BeautifulSoup, Tag
from Models.manga import Manga
from Models.chapter import Chapter


class MangaScraper:
    USER_AGENT: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0" 
    HEADERS: dict[str, str] = { "User-Agent" : USER_AGENT }
    url: str = "https://mangakatana.com/?search_by=book_name&search={}"
    mangas: list[Manga] = []
    chapters: list[Chapter] = []
    
    
    def __init__(self, args):
        self.args = args
    
    
    def search_manga_list(self, name: str) -> list[Manga]:
        book_list = self.get_soup(self.url.format(name)).find(id = "book_list")
        
        if isinstance(book_list, Tag):
            for item in book_list.find_all("div", {"class" : "item"}):
                mangaItem = item.find(class_ = "title").a
                self.mangas.append(Manga(mangaItem.text, mangaItem.get("href"), None))
        else:
            print("No valid mangas found.") # needs to change
            
        return self.mangas
    
    
    def search_manga_chapters(self, choice: int) -> list[Chapter]:
        table  = self.get_soup(self.mangas[choice].url).find(class_ = "chapters")

        if isinstance(table, Tag):
            for chapter in table.find_all("div", {"class": "chapter"}):
                self.chapters.append(Chapter(chapter.text, chapter.a.get("href")))
        else:
            print("No valid chapters table found.") # needs to change
            
        return self.chapters
            
            
    def get_soup(self, url) -> BeautifulSoup:
        r: Response = requests.get(url, headers = self.HEADERS)
        soup: BeautifulSoup = BeautifulSoup(r.text, "html.parser")
        
        return soup 
        