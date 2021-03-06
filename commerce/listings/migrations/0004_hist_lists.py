# Generated by Django 3.1.5 on 2021-03-06 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20210305_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='hist_lists',
            fields=[
                ('listingID', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('startingBid', models.FloatField(max_length=40)),
                ('finalBid', models.FloatField(max_length=40)),
                ('finalBidBy', models.CharField(max_length=40)),
                ('listBy', models.CharField(max_length=40)),
                ('createDateTime', models.CharField(max_length=40)),
            ],
        ),
    ]