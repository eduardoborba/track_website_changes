from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('scrapes_configuration/', include('scrapes_configuration.urls')),
    path('admin/', admin.site.urls),
    path('django-rq/', include('django_rq.urls'))
]
