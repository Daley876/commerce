# Generated by Django 3.1.5 on 2021-03-10 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_auto_20210307_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bids',
            name='datetimeOfBid',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetimeOfComment',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='hist_lists',
            name='closedDateTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
