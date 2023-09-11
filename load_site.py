"""
Author: SadSack963
Version: 1.0
Date: 10th September 2023

Use the get_webpage() function to download the raw HTML of a webpage and save it to a local file.

You can then do unlimited testing on that page by loading it from the local file,
which will save your own bandwidth and prevent multiple downloads from the server during code testing.

Hopefully this will prevent the website from blocking you or even introducing anti-robot measures in the future.
Another advantage is that the page will never change while you are testing it,
and it will always be there for comparison if the site changes and causes problems with your code later.

   Do not expect to be able to render this file properly.
   Resources such as images and CSS are on the server, not your hard drive!
   Just keep one copy of the page open in your browser so that you can use the development tools to search through it.
"""

# URL of the website we want to investigate
URL = "https://www.apartments.com/new-york-ny/"

# Create a "data" directory in the project tree
FILE_RAW = 'data/apartments.html'

# http://myhttpheader.com/
ACCEPT = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"

# User-Agent HTTP Headers
#   https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent
USER_AGENT = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41",
    "Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.2.15 Version/10.00",
    "Opera/9.60 (Windows NT 6.0; U; en) Presto/2.1.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)",
]


def get_webpage(url: str = URL, file: str = FILE_RAW, load_from_file: bool = True) -> str:
    """
    Function to get the HTML of a webpage.
    The function will first check the given URL against the Most Recently Used URL.
    If the URL is the same as previously used, and an HTML file exists and load_from_file is True,
    then the HTML is loaded from file.
    Otherwise, the HTML is downloaded from the given URL and saved to file.

    :param url: webpage URL - defaults to constant URL
    :type url: string
    :param file: path to HTML file - defaults to constant FILE_RAW
    :type file: string
    :param load_from_file: load webpage from file if available - defaults to True
    :type load_from_file: boolean
    :return: HTML of the webpage
    :rtype: string
    """
    import os

    # Check the most recently used URL
    same_address = False
    if os.path.exists(path="data/mru.txt"):
        with open(file="data/mru.txt", mode="r") as fp:
            mru = fp.readline().strip()
        if url == mru:
            same_address = True

    if same_address and os.path.exists(path=file) and load_from_file:
        print(
            f"Loading Webpage From File\n"
            f"{file}\n"
            f"===========================\n"
        )
        with open(file=file, mode='r', encoding='utf-8') as fp:
            html = fp.read()
    else:
        html = download_webpage(url=url, file=file)
        # Save the URL to the MRU file
        with open("data/mru.txt", mode="w") as fp:
            fp.write(url)

    return html


def download_webpage(url: str = URL, file: str = FILE_RAW) -> str:
    """
    Function to download the raw (unrendered) HTML code from a webpage.
    The HTML is saved in a file of your choice for future use, e.g. during code testing.
    To download a fresh copy of the web page, simply delete the existing file.

    :param url: webpage URL - defaults to constant URL
    :type url: string
    :param file: path to HTML file - defaults to constant FILE_RAW
    :type file: string
    :return: HTML downloaded from webpage
    :rtype: string
    """
    import requests
    from random import choice

    # Send a User-Agent string to avoid CAPTCHA
    headers = {
        'Accept': ACCEPT,
        'User-Agent': choice(USER_AGENT),
    }
    print(f'{headers = }\n')

    # Download the webpage
    print(
        "Retrieving Webpage from URL\n"
        f"{url}\n"
        "===========================\n"
    )
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()
    html = response.text

    print(
        f"Saving Webpage To File\n"
        f"{file}\n"
        f"===========================\n"
    )
    with open(file, mode='w', encoding='utf-8') as fp:
        fp.write(html)
    return html


if __name__ == "__main__":
    web_page = get_webpage(url=URL, file=FILE_RAW)
    print(web_page)
