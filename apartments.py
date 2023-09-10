from bs4 import BeautifulSoup
from load_site import get_webpage

URL = "https://www.apartments.com/san-francisco-ca/"
FILE = "data/apartments.html"

# TODO: Use BeautifulSoup/Requests to scrape all the listings from the apartments.com web address
soup = BeautifulSoup(markup=get_webpage(url=URL, file=FILE, load_from_file=True), features="html.parser")
# or using the default values...
# soup = BeautifulSoup(get_webpage(), "html.parser")
placard_container = soup.find(id="placardContainer")
property_information = placard_container.find_all("div", class_="property-information")

# TODO: Create a list of links for all the listings you scraped
property_links = [element.find("a", class_="property-link").get("href") for element in property_information]
# print(property_links)
# print(len(property_links))

# TODO: Create a list of prices for all the listings you scraped
top_level_infos = placard_container.find_all("div", class_="top-level-info")
property_prices = [element.find("p", class_="property-pricing").get_text() for element in top_level_infos]
# print(property_prices)
# print(len(property_prices))

# TODO: Create a list of addresses for all the listings you scraped
property_addresses = [element.find("div", class_="property-address").get("title") for element in property_information]
# print(property_addresses)
# print(len(property_addresses))
