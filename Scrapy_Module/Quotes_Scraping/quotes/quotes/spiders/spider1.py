import scrapy
import json
import time
import os

class QuotesSpider(scrapy.Spider):
    name ='quotes'

    def start_requests(self):
        
        urls = [
                'http://quotes.toscrape.com/page/1/',
                'http://quotes.toscrape.com/page/2/',]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    """            
    def parse(self, response):   # Terminal run cmd : scrapy crawl quotes
        page = response.url.split(".")[-2]
        filename = f'quotes-{page}.html'
        
        with open(filename, 'wb') as f:
            f.write(response.body)
        
        self.log(f'Saved file {filename}')
    """

    def parse(self, response):   # Terminal run cmd : scrapy crawl quotes -o quotes.json
        for quote in response.css('div.quote'):
            yield{
                'text': quote.css('span.text::text').get(),
                'author':  quote.css('small.author::text').get()
            }

    with open ('Quotes_Scraping/quotes/quotes.json') as jf:
        data = json.load(jf)
        count = 1
        for q1 in data:
            os.system("clear")
            print('*'*100)
            print("Quote {0}: \033[92m {1} \033[00m".format(count,q1['text']))
            print("\nAuthor: \033[93m {} \033[00m".format(q1['author']))
            print('*'*100)
            time.sleep(300) # delay in sec # Every cyclic time it display quote
            count +=1
os.system("clear")            
end_line = ["This is what we have, Thanks for reading Quotes, Adios."]*7

for i in range(7):
    print(end_line[i],  flush=True)
    time.sleep(2)
    os.system("clear")
    time.sleep(1)
            



