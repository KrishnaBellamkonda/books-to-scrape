import scrapy 
from scrapy.loader import ItemLoader
from paginations.items import Books, Genre

class GenreSpider(scrapy.Spider):
    name = "GenreSpider"

    def start_requests(self):
        urls = ["https://books.toscrape.com/"]
        for url in urls:
            yield scrapy.Request(url, callback=self.parseLinks)
    

    def parseLinks(self, response):
        genreLinksXPath = "//ul[@class='nav nav-list']/li/ul/li/a/@href"
        genreLinks = response.xpath(genreLinksXPath).extract()
        for href in genreLinks:
            print(response.urljoin(href))
            yield scrapy.Request(response.urljoin(href), callback=self.parseItems)

    def parseItems(self, response):
        articleXPath = "//article[@class='product_pod']"
        titleXPath = ".//h3/a/@title"
        priceXPath = ".//p[@class='price_color']"
        instockXPath = ".//p[contains(@class, 'availability')]"
        rating = ".//p[contains(@class, 'star-rating')]/@class"
        genre = response.xpath("//h1/text()").extract_first()
        for article in response.xpath(articleXPath):
            loader = ItemLoader(Genre(), response = response, selector=article)
            loader.add_xpath('title', titleXPath)
            loader.add_xpath('price', priceXPath)
            loader.add_xpath('instock', instockXPath)
            loader.add_xpath('rating', rating)
            loader.add_value('genre', genre)
            yield loader.load_item()
        
        # Pagination (next button)
        nextButtonXPath = "//li[@class='next']/a/@href"
        nextLinkAddress = response.xpath(nextButtonXPath).extract_first()
        if(nextLinkAddress is not None):
            nextLink = response.urljoin(nextLinkAddress)
            yield scrapy.Request(nextLink, callback = self.parseItems)