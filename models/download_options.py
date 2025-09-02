import argparse
from dataclasses import dataclass
from typing import Union
from models.enums.chapter_selection import ChapterSelection
from models.enums.information_output import InformationOutput


@dataclass
class DownloadOptions:
    name: str
    absolute: bool
    chapter_selection: Union[ChapterSelection, str]
    chapter_range: str
    chapter_pick: str
    latest: bool
    all: bool
    count: bool
    output_dir: str
    verbose: bool
    progress_bar: bool
    information_output: InformationOutput


    def __init__(self, args: argparse.Namespace):
        self.name = getattr(args, "name")
        self.absolute = getattr(args, "absolute")
        self.chapter_range = getattr(args, "range")
        self.chapter_pick = getattr(args, "pick")
        self.latest = getattr(args, "latest")
        self.all = getattr(args, "all")
        self.count = getattr(args, "count")
        self.verbose = getattr(args, "verbose")
        self.output_dir = getattr(args, "output")
        self.progress_bar = getattr(args, "progress")
