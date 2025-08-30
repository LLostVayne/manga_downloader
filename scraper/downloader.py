import os
import time
from bs4 import BeautifulSoup
from models.chapter import Chapter
from utils.exceptions import InvalidChapterType, NoResultsError
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
from utils.folder_manager import FolderManager
from utils.page_fetcher import fetch_page


class Downloader:
    def __init__(self):
        __chrome_options = Options()
        __chrome_options.add_experimental_option("detach", True)
        __chrome_options.add_argument("--log-level=3")
        __chrome_options.add_argument("--headless")
        LOGGER.setLevel(logging.ERROR)
        self.__driver = webdriver.Chrome(options=__chrome_options)
        self.__max_retries = 3

    def download_chapters(self, chapters: list[Chapter]):
        try:
            if isinstance(chapters, list):
                for chapter in chapters:
                    self.__driver.get(chapter.url)
                    soup = BeautifulSoup(self.__driver.page_source, "html.parser")

                    images = soup.find(id="imgs")
                    if not images:
                        raise NoResultsError("Couldn't find any images")

                    pages = images.find_all(id=re.compile("page\\d*"))
                    if not pages:
                        raise NoResultsError("Couldn't find any image pages")

                    FolderManager.create_folders(chapter.title.replace(":", ""))

                    for page in pages:
                        self.__download_chapter(page.img.get("data-src"))

                    os.chdir("..")
            else:
                raise InvalidChapterType("Chapters has to be of type list[Chapter]")
        finally:
            self.__driver.quit()



    def __download_chapter(self, url: str):
        for attempt in range(1, self.__max_retries + 1):
            soup, r = fetch_page(url)

            page_name: str = "page_" + re.search("\\d*.jpg", url).group()

            if r.status_code == 200:

                with open(page_name, "wb") as file:
                    file.write(r.content)

                if os.path.getsize(page_name) != 0:
                    break
                else:
                    print(f"Attempt {attempt} failed for downloading page: {page_name}")
                    time.sleep(2)
            else:
                print(f"Attempt {attempt} failed for downloading page: {page_name}")
                time.sleep(2)