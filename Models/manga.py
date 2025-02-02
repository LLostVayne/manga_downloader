from dataclasses import dataclass
from .chapter import Chapter

@dataclass
class Manga:
    title: str
    url: str
    chapters: list[Chapter] | None
    
    def __init__(self, title: str, url: str, chapters: list[Chapter] | None):
        self.title = title
        self.url = url
        self.chapters = chapters