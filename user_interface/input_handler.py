class InputHandler:
    
    def __init__(self, args):
        self.args = args

    
    def get_manga_search(self) -> str:
        manga: str = self.args.name or input("Which manga would you like to search? ")
    
        return manga
    
    
    def get_manga_to_download(self) -> int:
        choice =  int(input("Input number of manga you want to download\n?> "))
        
        return choice
    
    def get_chapter_selection(self):
        raise NotImplementedError