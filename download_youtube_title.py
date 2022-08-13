from bs4 import BeautifulSoup
import requests
import sys
url=str(sys.argv[1])

def scrape_info(url):
    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")
    title =s.find("meta", itemprop="name")['content']
    print(title)
  
title= scrape_info(url)
