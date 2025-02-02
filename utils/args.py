import argparse
import textwrap

def get_args() -> argparse.Namespace:
    
    parser = argparse.ArgumentParser(
        description="Download manga from 'Manga Katana' using the CLI or through the web",
        usage="%(prog)s [options]",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument("-n", metavar="<manga_name>", help="Name of the manga")
    parser.add_argument("-abs", metavar="", help="Will search for a 1:1 name")
    parser.add_argument("-l", metavar="", default=False, help="Download the latest chapter")
    parser.add_argument("-a", metavar="", default=False, help="Download all chapters")
    parser.add_argument("-c", metavar="", default=False, help="Show how many chapters were downloaded")
    parser.add_argument("-v", metavar="", default=False, help="Show detailed information")
    parser.add_argument("-o", metavar="<output_directory>", help="Directory output")
    parser.add_argument("-r", metavar="<1:4|:5|4:>", help="Specify range of chapters to download")
    
    bookmark = parser.add_argument_group(title="Bookmarkt Options")
    bookmark.add_argument("-BS", metavar="<bookmark_name>", help="Save the manga you are going to download in a bookmark")
    bookmark.add_argument("-BR", metavar="<bookmark_name>", help="Retrieve and download a saved bookmark")
    bookmark.add_argument("-BD", metavar="<bookmark_name>", help="Delete a saved bookmark")
    bookmark.add_argument("-BU", metavar="<bookmark_name>", help="Update a saved bookmark")
    bookmark.add_argument("-BL", metavar="<bookmark_name>", help="List all saved bookmarks")

    return parser.parse_args()