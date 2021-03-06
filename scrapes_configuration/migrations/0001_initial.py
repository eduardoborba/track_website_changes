# Generated by Django 3.2 on 2021-04-28 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapeTarget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scrape_url', models.CharField(max_length=1024)),
                ('scrape_selector', models.CharField(max_length=1024)),
                ('last_scraped', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ScrapeResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scrape_content', models.CharField(max_length=65536)),
                ('scrape_time', models.DateTimeField()),
                ('scrape_target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrapes_configuration.scrapetarget')),
            ],
        ),
    ]
