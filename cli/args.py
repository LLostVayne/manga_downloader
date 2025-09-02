import argparse

def get_args() -> argparse.Namespace:
    
    parser = argparse.ArgumentParser(
        description="Download manga from 'Manga Katana' using the CLI or through the web",
        usage="%(prog)s [options]",
        formatter_class=argparse.RawTextHelpFormatter
    )

    chapter_selection_exclusivity = parser.add_mutually_exclusive_group()
    information_output_exclusivity = parser.add_mutually_exclusive_group()

    parser.add_argument("-n","--name", help="Name of the manga")
    parser.add_argument("-abs","--absolute", action="store_true", help="Will search for a 1:1 name")
    chapter_selection_exclusivity.add_argument("-r", "--range", metavar="<1:4|:5|4:|3>", help="Specify range of chapters to download")
    chapter_selection_exclusivity.add_argument("-l","--latest", action="store_true", help="Download the latest chapter")
    chapter_selection_exclusivity.add_argument("-a","--all", action="store_true", help="Download all chapters")
    chapter_selection_exclusivity.add_argument("-p","--pick", metavar="<1,6,10,40>", help="Download selected chapters")
    parser.add_argument("-c","--count", action="store_true", help="Show how many chapters were downloaded")
    information_output_exclusivity.add_argument("-v","--verbose", action="store_true", help="Show detailed information")
    parser.add_argument("-o","--output", metavar="<output_directory>", help="Directory output")
    # parser.add_argument("--url", metavar="<https://mangakatana.com/...>", help="Download directly from a manga chapter list or manga chapter URL page")
    # parser.add_argument("--read", metavar="<input.txt>", help="Read a txt file with manga URL pages")
    information_output_exclusivity.add_argument("--progress", action="store_true", help="Show progress bar") # make mutually_exclusive_group for progress and verbose (maybe)
    # parser.add_argument("--proxy", metavar="<proxy_address>", help="Proxy address")

    bookmark = parser.add_argument_group(title="Bookmark Options")
    bookmark.add_argument("--bm-save", metavar="<name>", help="Save the manga you are going to download in a bookmark")
    bookmark.add_argument("--bm-retrieve", metavar="<name>", help="Retrieve and download a saved bookmark")
    bookmark.add_argument("--bm-delete", metavar="<name>", help="Delete a saved bookmark")
    bookmark.add_argument("--bm-update", metavar="<name>", help="Update a saved bookmark")
    bookmark.add_argument("--bm-list", action="store_true", help="List all saved bookmarks")

    return parser.parse_args()