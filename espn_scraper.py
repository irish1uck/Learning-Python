

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# opening up the connection and grabbing the page
my_url = "https://www.espn.com/"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")
head_lines = page_soup.findAll("section", {"class":"headlineStack__listContainer"})

filename = "sports_today.csv"
f = open(filename, "w")

headers = "title, link\n"

f.write(headers)

story = head_lines[0]
for story in head_lines:
      title = story.li.a.text
      link = story.li.a["href"]

      print("Story: " + title)
      print("Link: " + link)
      f.write(title + "," + link + "\n")

f.close()      
