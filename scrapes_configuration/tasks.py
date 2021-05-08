from models import ScrapeTarget, ScrapeResult
import requests


def enqueue_all_targets():
    targets = ScrapeTarget.objects.all()

    for target in targets:
        requests.post('http://localhost:6800/schedule.json',
            params={ 'project':'default', 'spider': 'main_spider' })

def check_scraper_finished():
    targets = ScrapeTarget.objects.all()

    for target in targets:
        results = target.scraperesult_set.order_by('-scrape_time')[:2]
