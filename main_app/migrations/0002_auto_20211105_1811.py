# Generated by Django 3.2.7 on 2021-11-05 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='itinerary',
        ),
        migrations.AddField(
            model_name='itinerary',
            name='locations',
            field=models.ManyToManyField(to='main_app.Location'),
        ),
    ]
