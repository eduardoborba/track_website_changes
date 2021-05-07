import scrapy
from scraper.items import ScraperItem
from datetime import datetime
from scrapes_configuration.models import ScrapeTarget


class MainSpider(scrapy.Spider):
  name = "main_spider"
  start_urls = ["https://brasil.diplo.de/br-pt/coronavirus/2320108"]

  def parse(self, response):
      item = ScraperItem()
      item["scrape_target"] = ScrapeTarget.objects.get(scrape_url=response.url)
      item["scrape_content"] = response.css(".c-rte--default p.rte__paragraph").get()
      item["scrape_time"] = str(datetime.utcnow())
      yield item
