# Generated by Django 3.1.5 on 2021-03-10 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_auto_20210309_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bids',
            name='datetimeOfBid',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetimeOfComment',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='hist_lists',
            name='closedDateTime',
            field=models.DateTimeField(),
        ),
    ]