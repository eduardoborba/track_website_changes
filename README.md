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
