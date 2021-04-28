from django.contrib import admin

from .models import ScrapeTarget
from .models import ScrapeResult

admin.site.register(ScrapeTarget)
admin.site.register(ScrapeResult)
