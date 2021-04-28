from django.db import models

class ScrapeTarget(models.Model):
    scrape_url = models.CharField(max_length=1024)
    scrape_selector = models.CharField(max_length=1024)
    last_scraped = models.DateTimeField()

class ScrapeResult(models.Model):
    scrape_target = models.ForeignKey(ScrapeTarget, on_delete=models.CASCADE)
    scrape_content = models.CharField(max_length=65536)
    scrape_time = models.DateTimeField()
