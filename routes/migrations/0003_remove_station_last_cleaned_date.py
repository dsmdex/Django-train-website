# Generated by Django 5.1.7 on 2025-03-19 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0002_station_last_cleaned_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='last_cleaned_date',
        ),
    ]
