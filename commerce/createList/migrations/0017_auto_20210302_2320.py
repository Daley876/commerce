# Generated by Django 3.1.5 on 2021-03-03 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createList', '0016_auto_20210301_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bid',
            field=models.DecimalField(decimal_places=2, max_digits=9999999999.99),
        ),
    ]
