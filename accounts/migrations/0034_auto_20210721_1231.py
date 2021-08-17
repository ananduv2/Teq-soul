# Generated by Django 3.2.3 on 2021-07-21 07:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_auto_20210721_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='datetime',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 7, 21, 12, 31, 45, 314966), null=True),
        ),
        migrations.AlterField(
            model_name='query',
            name='message',
            field=models.TextField(max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='query',
            name='reply',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
    ]