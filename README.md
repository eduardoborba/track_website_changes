# Track Website Changes

This is an experimental project that aims in building a web interface to
setup different scraping targets to track. Basically, if you want to track
changes in a specific area of a website, let's say looking for appointments
for something, you could setup a new scraping target with a URL and a selector
and when the content in that area of that website changes you will be notified somehow.

# Running django server

```
python manage.py runserver
```

# Running migrations

```
python manage.py makemigrations scrapes_configuration
python manage.py migrate
```

# Running background jobs

```
python manage.py rqworker
python manage.py rqscheduler
```

# Running scrapyd

```
cd scraper
scrapyd
```

# Useful links

## Background jobs

[http://localhost:8000/django-rq/](http://localhost:8000/django-rq/)

## Admin page

[http://localhost:8000/admin/](http://localhost:8000/admin/)
