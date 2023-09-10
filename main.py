from load_site import get_webpage
from apartments import get_property_details
URL = "https://www.apartments.com/san-francisco-ca/"
FILE = "data/apartments.html"

# TODO: Use requests to get the web page
html = get_webpage(url=URL, file=FILE)

# TODO: Use BeautifulSoup to scrape all the listings from the web page
property_links, property_prices, property_addresses = get_property_details()
