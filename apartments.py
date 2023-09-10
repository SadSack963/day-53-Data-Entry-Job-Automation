from bs4 import BeautifulSoup
from load_site import get_webpage

URL = "https://www.apartments.com/san-francisco-ca/"
FILE = "data/apartments.html"

soup = BeautifulSoup(markup=get_webpage(url=URL, file=FILE), features="html.parser")



