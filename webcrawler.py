"""Crawl a web-site.

Fetch contnt from a URL. Extract the hyperliks and recurse (i.e. fetch
the contnt of the hyperlink URLs and extract their hyperlinks and recurse).

This code only works with Python 2.
"""

import sys
import argparse
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen
import re

def extract_hyperlinks(content):
    """Returns a list of hyperlinks."""
    #Regular expression, note that the group used to identify the hyperlink
    #uses the non-greedy version of the '*' (Repeat matching) special character.
    hyperlinks = re.findall(r'<a href="(.*?)".*>', content)
    return hyperlinks


def fetch_content(url):
    """Return the content from a URL."""
    handle = urlopen(url)
    bstring = handle.read()
    return str(bstring)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    args = parser.parse_args()

    content = fetch_content(args.url)
    hyperlinks = extract_hyperlinks(content)

    for hlink in hyperlinks:
        print(hlink)

if __name__ == "__main__":
    main()
