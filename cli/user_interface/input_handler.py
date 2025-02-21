class InputHandler:
    
    def __init__(self, args):
        self.args = args

    
    def get_manga_search(self) -> str:
        manga: str = self.args.n or input("Which manga would you like to search? ")

        return manga
    
    
    def get_manga_to_download(self) -> int:
        choice =  int(input("Select manga: "))
        
        return choice
    
    
    def get_chapter_selection(self) -> str:
        chapters = input("Input number of manga(s) you want to download\n1: | :2 | 1:4 | 4 | all\n?> ")
        
        return chapters