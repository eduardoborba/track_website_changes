# Generated by Django 3.2 on 2021-05-07 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapes_configuration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapetarget',
            name='last_scraped',
            field=models.DateTimeField(null=True),
        ),
    ]