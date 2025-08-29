import argparse
from dataclasses import dataclass
from typing import Union
from models.chapter_selection import ChapterSelection


@dataclass
class DownloadOptions:
    name: str
    absolute: bool
    chapter_selection: Union[ChapterSelection, str]
    chapter_range: str
    latest: bool
    all: bool
    count: bool
    verbose: bool
    output_dir: str


    def __init__(self, args: argparse.Namespace):
        self.name = getattr(args, "name")
        self.absolute = getattr(args, "absolute")
        self.chapter_range = getattr(args, "range")
        self.latest = getattr(args, "latest")
        self.all = getattr(args, "all")
        self.count = getattr(args, "count")
        self.verbose = getattr(args, "verbose")
        self.output_dir = getattr(args, "output")