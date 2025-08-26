from dataclasses import dataclass

@dataclass
class MediaItem:
    title: str
    url: str

    def __init__(self, title: str, url: str):
        self.title = title
        self.url = url
