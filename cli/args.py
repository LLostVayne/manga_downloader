import argparse
import textwrap

def get_args() -> argparse.Namespace:
    
    parser = argparse.ArgumentParser(
        description="Download manga from 'Manga Katana' using the CLI or through the web",
        usage="%(prog)s [options]",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    exclusivity = parser.add_mutually_exclusive_group()
    
    parser.add_argument("-n","--name", help="Name of the manga")
    parser.add_argument("-abs","--absolute", action="store_true", help="Will search for a 1:1 name")
    exclusivity.add_argument("-l","--latest", action="store_true", help="Download the latest chapter")
    exclusivity.add_argument("-a","--all", action="store_true", help="Download all chapters")
    parser.add_argument("-c","--count", action="store_true", help="Show how many chapters were downloaded")
    parser.add_argument("-v","--verbose", action="store_true", help="Show detailed information")
    parser.add_argument("-o", metavar="<output_directory>", help="Directory output")
    exclusivity.add_argument("--range", metavar="<1:4|:5|4:>", help="Specify range of chapters to download")
    # parser.add_argument("--url", metavar="<https://mangakatana.com/...>", help="Download directly from a manga URL page")
    # parser.add_argument("--read", metavar="<input.txt>", help="Read a txt file with manga URL pages")
    
    bookmark = parser.add_argument_group(title="Bookmarkt Options")
    bookmark.add_argument("-BS", metavar="<bookmark_name>", help="Save the manga you are going to download in a bookmark")
    bookmark.add_argument("-BR", metavar="<bookmark_name>", help="Retrieve and download a saved bookmark")
    bookmark.add_argument("-BD", metavar="<bookmark_name>", help="Delete a saved bookmark")
    bookmark.add_argument("-BU", metavar="<bookmark_name>", help="Update a saved bookmark")
    bookmark.add_argument("-BL", metavar="<bookmark_name>", help="List all saved bookmarks")

    return parser.parse_args()