# Generated by Django 3.2 on 2021-04-08 13:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20210408_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 10, 13, 8, 15, 390445, tzinfo=utc)),
        ),
    ]