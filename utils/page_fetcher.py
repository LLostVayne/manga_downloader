import requests
from bs4 import BeautifulSoup
from requests import Response
from utils.constants import HEADERS

def fetch_page(url: str) -> tuple[BeautifulSoup, Response]:
    """
    Fetches url page and returns a tuple of a Soup and Response

    :param url: Url to fetch.
    :return: Returns a BeautifulSoup and Response
    """

    r: Response = requests.get(url, headers=HEADERS, timeout=10)
    r.raise_for_status()
    soup: BeautifulSoup = BeautifulSoup(r.text, "html.parser")

    return soup, r
