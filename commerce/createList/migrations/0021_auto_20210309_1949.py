# Generated by Django 3.1.5 on 2021-03-10 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createList', '0020_listing_currbidby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='createDateTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]