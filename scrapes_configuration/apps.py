from django.apps import AppConfig
import datetime
from redis import Redis
from rq import Queue
from rq_scheduler import Scheduler


class ScrapesConfigurationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scrapes_configuration'


    def ready(self):
        queue = Queue('default', connection=Redis())
        scheduler = Scheduler(queue=queue)

        scheduler.schedule(
            scheduled_time=datetime.utcnow(), # Time for first execution, in UTC timezone
            func='enqueue_all_targets',       # Function to be queued
            interval=60,                      # Time before the function is called again, in seconds
        )
