import argparse

# class DownloadOptions:
#     name: str
#     chapter_selection: str = "" # range | latest | all
#     count: bool
#     verbose: bool
#     output_dir: str

class DownloadOptions:
    name: str
    chapter_selection: str = ""  # range | latest | all
    count: bool
    verbose: bool
    output_dir: str

    # Initialize optional arguments
    def __init__(self, args: argparse.Namespace):
        self.count = args.count
        self.verbose = args.verbose
        # self.output_dir = args.output_dir