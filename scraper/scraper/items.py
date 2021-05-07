# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from scrapes_configuration.models import ScrapeResult
# from scrapes_configuration.models import ScrapeTarget

class ScraperItem(DjangoItem):
    django_model = ScrapeResult
