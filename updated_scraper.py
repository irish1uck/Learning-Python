

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# opening up the connection and grabbing the page
my_url = "https://www.espn.com"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")
quick_links = page_soup.findAll("li", {"class":"quicklinks_list__item"})
