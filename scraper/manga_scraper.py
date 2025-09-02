from bs4 import Tag
from models.media.manga import Manga
from models.media.chapter import Chapter
from utils.exceptions import NoResultsError
from utils.page_fetcher import fetch_page


class MangaScraper:
    """The MangaScraper class is used to scrape data for the manga(s) and the chapter(s)."""

    def __init__(self):
        self.__url: str = "https://mangakatana.com/?search_by=book_name&search={}"

    def fetch_found_mangas(self, title: str) -> list[Manga]:
        """
        Searches MangaKatana for the provide manga title.
        Raises an error if no results were found.
        If the manga title is unique the site will redirect to the manga page immediately so it grabs the response.url instead of parsing for it.

        :param title: Name of the manga.
        :raise NoResultsError: If no results were found.
        :return: Returns a list of manga(s)
        """

        soup, response = fetch_page(self.__url.format(title))
        book_list = soup.find(id="book_list")
        mangas: list[Manga] = []

        if book_list is not None and "Not found any results" in book_list.text.strip():
            raise NoResultsError("No mangas found.")
        elif isinstance(book_list, Tag):
            for item in book_list.find_all("div", {"class": "item"}):
                manga_item = item.find(class_="title").a
                cover_image = item.find(class_="wrap_img").img.get("src")
                mangas.append(Manga(
                        title=manga_item.text,
                        url=manga_item.get("href"),
                        cover_image=cover_image,
                    ))
        else:
            cover_image = soup.find(class_="cover").img.get("src")
            mangas.append(Manga(
                title=title,
                url=response.url,
                cover_image=cover_image
            ))

        return mangas


    def search_chapters(self, chosen_manga: Manga) -> list[Chapter]:
        """
        Searches the chapter page for all the chapters.
        Raises an error if no chapters were found.

        :param chosen_manga: Chosen manga to scrape.
        :raise NoResultsError: If no results were found.
        :return: Returns a list of chapters.
        """
        soup = fetch_page(chosen_manga.url)[0]
        table = soup.find(class_="chapters")
        chapters: list[Chapter] = []

        if isinstance(table, Tag):
            for chapter in table.find_all("div", {"class": "chapter"}):
                chapters.append(Chapter(chapter.text, chapter.a.get("href")))

            return list(reversed(chapters))
        else:
            raise NoResultsError("No chapters found.")  # Needs to change
