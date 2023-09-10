from bs4 import BeautifulSoup
from load_site import get_webpage

URL = "https://www.apartments.com/san-francisco-ca/"
FILE = "data/apartments.html"

# TODO: Use BeautifulSoup/Requests to scrape all the listings from the apartments.com web address
soup = BeautifulSoup(markup=get_webpage(url=URL, file=FILE, load_from_file=True), features="html.parser")
# or using the default values...
# soup = BeautifulSoup(get_webpage(), "html.parser")

# TODO: Create a list of links for all the listings
placard_container = soup.find(id="placardContainer")
property_information = placard_container.find_all("div", class_="property-information")
property_links = [element.find("a", class_="property-link").get("href") for element in property_information]
# print(property_links)
# print(len(property_links))
