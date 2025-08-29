from models.media_item import MediaItem


class OutputHandler:
    
    @staticmethod
    def show_columns(data: list[MediaItem]) -> None:
        for index, value in enumerate(data):
            print(f"[{index}] {value.title}")