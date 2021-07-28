# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

def cleanRating(value):
    numberInText =  value.replace('star-rating', '').strip()
    textToNumberDict = {
        "One":1, 
        "Two":2, 
        "Three":3, 
        "Four":4, 
        "Five":5
    }
    return textToNumberDict[numberInText]

removePound = lambda x: x.replace(u"\u00a3", '').strip()
instockCleaning = lambda x: x.replace("\n", '').strip()

class Books(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field(
        output_processor = TakeFirst()
    )
    rating = scrapy.Field(
        input_processor = MapCompose(cleanRating),
        output_processor = TakeFirst()
    )
    price = scrapy.Field(
        input_processor = MapCompose(remove_tags, removePound), 
        output_processor = TakeFirst()
    )
    instock = scrapy.Field(
        input_processor = MapCompose(remove_tags, instockCleaning),
        output_processor = TakeFirst()
    )

class Genre(scrapy.Item):
    genre = scrapy.Field()
    title = scrapy.Field(
        output_processor = TakeFirst()
    )
    rating = scrapy.Field(
        input_processor = MapCompose(cleanRating),
        output_processor = TakeFirst()
    )
    price = scrapy.Field(
        input_processor = MapCompose(remove_tags, removePound), 
        output_processor = TakeFirst()
    )
    instock = scrapy.Field(
        input_processor = MapCompose(remove_tags, instockCleaning),
        output_processor = TakeFirst()
    )