class InputHandler:
    
    def __init__(self, args):
        self.args = args

    
    def get_manga_name(self) -> str:
        manga: str = input("Which manga would you like to search? ")

        return manga
    
    
    def get_manga_selection(self) -> int:
        selection: int =  int(input("Select manga: "))
        
        return selection
    
    
    def download_all_chapters(self) -> None:
        download_all: str = input("Download all chapters?[y/n] ")
        
        self.args.all = download_all == "y"
        # return download_all == "y"
    
    
    def download_latest_chapter(self) -> None:
        download_latest: str = input("Download latest chapter?[y/n] ")
        
        self.args.latest = download_latest == "y"
        # return download_latest == "y"
    
    
    def get_chapter_selection(self) -> str | None:
        chapters: str = input("Input number of chapter(s) you want to download\n1: | :2 | 1:4 | 4 \n?> ")
       
        self.args.range = chapters if chapters != "" else None 
        # return chapters if chapters != "" else None
        
        