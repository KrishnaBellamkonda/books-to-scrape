# books-to-scrape
This is a scrapy web scraping project that was built to improve scrapy skills. 

### Setup 
* Install Scrapy
* Clone the repository 
* You can run `scrapy crawl GenreSpider -o data/filename.[csv/json]` to scrape and download the data


### Functionality 
This spider obtains the books.toscrap website and extracts data from it. 

### Modules 
* scrapy 
* os
* json

### Data Sample

* data/cleaned.json
```
{"title": "A Light in the Attic", 
"price": "51.77", 
"instock": "In stock", 
"rating": 3},


```


### Sources
* Scrapy installation (https://docs.scrapy.org/en/latest/intro/install.html)
* GoodReads Quotes website (https://www.goodreads.com/quotes)

