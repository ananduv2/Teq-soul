# Generated by Django 3.2.5 on 2021-08-03 14:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0070_auto_20210803_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificatetemplate',
            name='name',
            field=models.CharField(default='sample', max_length=100),
        ),
        migrations.AlterField(
            model_name='query',
            name='datetime',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 8, 3, 19, 43, 35, 437671), null=True),
        ),
    ]