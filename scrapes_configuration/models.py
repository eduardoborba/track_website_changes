from django.db import models


# scrape_target = ScrapeTarget(scrape_url='https://brasil.diplo.de/br-pt/coronavirus/2320108', scrape_selector='.c-rte--default p.rte__paragraph')
# scrape_target.save()
class ScrapeTarget(models.Model):
    scrape_url = models.CharField(max_length=1024)
    scrape_selector = models.CharField(max_length=1024)
    last_scraped = models.DateTimeField(null=True)

class ScrapeResult(models.Model):
    scrape_target = models.ForeignKey(ScrapeTarget, on_delete=models.CASCADE)
    scrape_content = models.CharField(max_length=65536)
    scrape_time = models.DateTimeField()
