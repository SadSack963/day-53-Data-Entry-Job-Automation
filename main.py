from load_site import get_webpage
from apartments import get_property_details

URL = "https://www.apartments.com/min-1-bedrooms-under-3000/?bb=y_7o1045zOv48mjoC"
FILE = "data/apartments.html"

# TODO: Use requests to get the web page
html = get_webpage(url=URL, file=FILE)

# TODO: Use BeautifulSoup to scrape all the listings from the web page
property_links, property_prices, property_addresses = get_property_details(html=html)

print(property_links)
print(property_prices)
print(property_addresses)
