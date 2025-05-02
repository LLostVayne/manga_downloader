

class DownloadOptions:
    name: str
    chapter_selection: str = "" # range | latest | all
    count: bool
    verbose: bool
    output_dir: str

