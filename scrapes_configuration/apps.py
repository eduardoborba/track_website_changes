from django.apps import AppConfig
import django_rq


class ScrapesConfigurationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scrapes_configuration'
