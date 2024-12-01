import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site, filename):
        self.site = site 
        self.filename = filename

    def scrape(self): 
        r = urllib.request.urlopen(self.site)
                            
        xml = r.read()
                             
        
        parser = "html.parser"
        sp = BeautifulSoup(xml, parser) 
        
        with open(self.filename, 'w', encoding='utf-8') as file:
            for item in sp.find_all("item"):
                title = item.find('title')
                if title is None:
                    continue
                else:
                    file.write('\n' + title.text + '\n')
                    print(title.text + '\n')


news = "https://news.google.com/news/rss/headlines"
Scraper(news, 'news.txt').scrape()
