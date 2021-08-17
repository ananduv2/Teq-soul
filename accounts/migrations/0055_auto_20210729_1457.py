# Generated by Django 3.2.5 on 2021-07-29 09:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0054_auto_20210727_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='sex',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='query',
            name='datetime',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 7, 29, 14, 57, 17, 328408), null=True),
        ),
    ]
