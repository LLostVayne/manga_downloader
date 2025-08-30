import os
import time
from bs4 import BeautifulSoup
from requests import Response
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.remote_connection import LOGGER
from models.chapter import Chapter
from utils.exceptions import InvalidChapterType, NoResultsError, DownloadError
import re
import logging
from utils.folder_manager import FolderManager
from utils.page_fetcher import fetch_image


class Downloader:
    def __init__(self):
        chrome_options = Options()
        # chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--log-level=3")
        # chrome_options.add_argument("--headless")
        LOGGER.setLevel(logging.ERROR)
        self.__driver = webdriver.Chrome(options=chrome_options)
        self.__max_retries = 5

    def download_chapters(self, chapters: list[Chapter]) -> None:
        try:
            if isinstance(chapters, list):
                for chapter in chapters:
                    self.__driver.get(chapter.url)

                    WebDriverWait(self.__driver, 10).until(
                        EC.presence_of_element_located((By.ID, "imgs"))
                    )

                    soup = BeautifulSoup(self.__driver.page_source, "html.parser")

                    images = soup.find(id="imgs")
                    if not images:
                        raise NoResultsError("Couldn't find any images")

                    image_pages = images.find_all(id=re.compile("page\\d*"))
                    if not image_pages:
                        raise NoResultsError("Couldn't find any image pages")

                    FolderManager.create_folders(chapter.title.replace(":", ""))

                    for id, page in enumerate(image_pages):
                        self.__download_chapter(page.img.get("data-src"), id)

                    os.chdir("..")
            else:
                raise InvalidChapterType("Chapters has to be of type list[Chapter]")
        finally:
            self.__driver.quit()


    def __download_chapter(self, url: str, id: int) -> None:
        page_name: str = f"page_{id}{re.search(".(?:jpg|jpeg|png|webp)", url).group()}"

        for attempt in range(1, self.__max_retries + 1):
            r: Response = fetch_image(url)

            if r.status_code == 200:
                with open(page_name, "wb") as file:
                    file.write(r.content)

                if os.path.getsize(page_name) > 0:
                    break
                else:
                    print(f"Attempt {attempt} failed for downloading page: {page_name}.")
            else:
                print(f"Attempt {attempt} failed for downloading page: {page_name} with HTTP code {r.status_code}.")

            if attempt < self.__max_retries:
                time.sleep(2)

        if os.path.getsize(page_name) == 0:
            raise DownloadError(f"Failed to download {page_name} from {url} with {self.__max_retries} attempts.")