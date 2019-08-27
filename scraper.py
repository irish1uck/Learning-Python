


import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

class Scraper:
    def __init__(self, site):
        self.site = site
    
    def scrape(self):
        r = uReq(self.site)
        html = r.read()
        parser = "html.parser"
        sp = soup(html, parser)
        for tag in sp.findAll("link"):
            url = tag.get("rel")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)
                
news = "https://www.cnn.com/"
scr = Scraper(news)
final = scr.scrape()
print(final)
