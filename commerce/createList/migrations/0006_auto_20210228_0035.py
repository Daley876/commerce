# Generated by Django 3.1.5 on 2021-02-28 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createList', '0005_auto_20210227_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]