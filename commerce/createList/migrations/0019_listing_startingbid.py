# Generated by Django 3.1.5 on 2021-03-06 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createList', '0018_auto_20210302_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='startingBid',
            field=models.FloatField(default=0.0),
        ),
    ]
