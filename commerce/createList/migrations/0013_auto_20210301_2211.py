# Generated by Django 3.1.5 on 2021-03-02 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createList', '0012_listing_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='createDateTime',
            field=models.CharField(blank=True, default='NONE', max_length=60),
        ),
    ]