import scrapy 
from scrapy.loader import ItemLoader
from paginations.items import Books

class ItemScraper(scrapy.Spider):
    name = "BookScraper"
    # Start URLs 
    start_urls = ['https://books.toscrape.com/']
    
    # Other urls 
    

    def parse(self, response):
        articleXPath = "//article[@class='product_pod']"
        titleXPath = ".//h3/a/@title"
        priceXPath = ".//p[@class='price_color']"
        instockXPath = ".//p[contains(@class, 'availability')]"
        rating = ".//p[contains(@class, 'star-rating')]/@class"
        for article in response.xpath(articleXPath):
            loader = ItemLoader(Books(), response = response, selector=article)
            loader.add_xpath('title', titleXPath)
            loader.add_xpath('price', priceXPath)
            loader.add_xpath('instock', instockXPath)
            loader.add_xpath('rating', rating)
            yield loader.load_item()
        
        # Pagination (next button)
        nextButtonXPath = "//li[@class='next']/a/@href"
        nextLinkAddress = response.xpath(nextButtonXPath).extract_first()
        if(nextLinkAddress is not None):
            nextLink = response.urljoin(nextLinkAddress)
            yield scrapy.Request(nextLink)

            
            
            

        