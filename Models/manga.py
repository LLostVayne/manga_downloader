from typing import Union

from .chapter import Chapter
from .media_item import MediaItem
from dataclasses import dataclass

@dataclass
class Manga(MediaItem):
    cover_image: str
    chapters: Union[Chapter, list[Chapter]] = None

    def __post_init__(self):
        pass