# Generated by Django 3.1.5 on 2021-02-28 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('title', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('bid', models.FloatField()),
                ('url', models.TextField(max_length=250)),
            ],
        ),
    ]
