# Generated by Django 3.1.5 on 2021-03-02 04:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('createList', '0016_auto_20210301_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='watcherList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listID', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='createList.listing')),
                ('userID', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]