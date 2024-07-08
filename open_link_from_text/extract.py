#!/usr/local/Caskroom/miniforge/base/bin/python
import re
import pyperclip
from urllib.parse import urlparse


def extract_urls():
    # Get the text from the clipboard
    text = pyperclip.paste()

    # Regular expression to match URLs in the text
    url_regex = r"(?P<url>https?://[^\s)]+)"

    # Find all matches of the URL regex in the text
    urls = re.findall(url_regex, text)

    # Parse the URLs using urlparse to make sure they are valid
    valid_urls = []
    for url in urls:
        try:
            parsed_url = urlparse(url)
            if parsed_url.scheme and parsed_url.netloc:
                valid_urls.append(url)
        except:
            pass

    return valid_urls


if __name__ == "__main__":
    print(' '.join(extract_urls()))
