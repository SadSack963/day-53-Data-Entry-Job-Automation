"""
Author: SadSack963
Version: 1.0
Date: 10th September 2023

Scrape property details from a webpage using BeautifulSoup.
"""

from bs4 import BeautifulSoup


def get_property_details(html: str) -> tuple:
    """
    Uses BeautifulSoup to parse a web page and extract property details.

    :param html: raw HTML of the web page
    :type html: string
    :return: tuple containing links, prices and addresses for the properties
    """

    # TODO: Use BeautifulSoup to scrape all the listings from the web page
    soup = BeautifulSoup(markup=html, features="html.parser")

    # Find the relevant sections of property information
    placard_container = soup.find(id="placardContainer")
    property_information_list = placard_container.find_all(name="div", class_="property-information")
    top_level_info_list = placard_container.find_all(name="div", class_="top-level-info")

    # TODO: Create a list of links for all the listings you scraped
    property_links = [element.find(name="a", class_="property-link").get("href")
                      for element in property_information_list]

    # TODO: Create a list of prices for all the listings you scraped
    property_prices = [element.find(name="p", class_="property-pricing").get_text()
                       for element in top_level_info_list]

    # TODO: Create a list of addresses for all the listings you scraped
    property_addresses = [element.find(name="div", class_="property-address").get("title")
                          for element in property_information_list]

    return property_links, property_prices, property_addresses


if __name__ == "__main__":
    with open(file="data/apartments.html", mode="r") as fp:
        web_page = fp.read()
    property_details = get_property_details(html=web_page)
    print(property_details)
