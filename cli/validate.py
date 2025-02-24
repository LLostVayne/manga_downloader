from .input_handler import InputHandler
from .output_handler import OutputHandler
from models.manga import Manga
from .chapter_selection import ChapterSelection
 
class Validate:
    """The Validate class is used to validate values between the flag and interactive mode of the application"""
    
    def __init__(self, args, input_handler, output_handler) -> None:
        self.args = args
        self.input: InputHandler = input_handler
        self.output: OutputHandler = output_handler

    
    
    def validate_name_selection(self) -> str:
        return self.input.get_manga_name() if self.args.name is None else self.args.name
    
    
    
    def validate_manga_selection(self, mangas: list[Manga]) -> int:
        selection: int = 0
        
        if (not self.args.absolute and len(mangas) > 1): # Not absolute and list the mangas
            self.output.show_columns(mangas)
            selection: int = self.input.get_manga_selection()
        elif (self.args.absolute and len(mangas) > 1): # Absolute and loop through list in order to find 1:1 manga title
            for index, manga in enumerate(mangas):
                if (manga.title.lower() == self.args.name.lower()):
                    selection = index
        else: # One manga and/or absolute
            selection = 0
        
        return selection
    
    
    def validate_all_selection(self) -> None:
        if (not self.args.all):
            self.input.download_all_chapters()    
        #  if self.args.all is False else self.args.all
    
    
    def validate_latest_selection(self) -> None:
        if (not self.args.latest):
            self.input.download_latest_chapter()    
        #  if self.args.latest is False else self.args.latest


    def validate_range_selection(self) -> str | None:
        return self.input.get_chapter_selection() if self.args.range is None else self.args.range

    
    def validate_chapter_selection(self):
        if (self.args.range is None and not self.args.latest and not self.args.all):
            self.validate_range_selection()
        elif (not self.args.latest and self.args.range is None and not self.args.all):
            self.validate_latest_selection()
        elif (not self.args.all and self.args.range is None and not self.args.latest):
            self.validate_all_selection()
        
        
        # if (self.validate_all_selection()):
        #     return ChapterSelection.ALL
        # elif (self.validate_latest_selection()):
        #     return ChapterSelection.LATEST
        # elif (self.validate_range_selection()):
        #     return ChapterSelection.RANGE
    
        

    def validate_missing_args(self):
        self.validate_name_selection()