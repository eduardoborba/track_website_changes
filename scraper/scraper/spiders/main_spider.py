import scrapy
from scraper.items import ScraperItem
from datetime import datetime


class MainSpider(scrapy.Spider):
  name = "main_spider"
  start_urls = ["https://brasil.diplo.de/br-pt/coronavirus/2320108"]

  def parse(self, response):
      item = {}
      item["scrape_target"] = 1
      item["scrape_content"] = response.css(".c-rte--default p.rte__paragraph").get()
      item["scrape_time"] = str(datetime.utcnow())
      yield item
