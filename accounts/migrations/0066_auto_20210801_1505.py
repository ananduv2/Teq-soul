# Generated by Django 3.2.5 on 2021-08-01 09:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0065_auto_20210801_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='project_file',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='query',
            name='datetime',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 8, 1, 15, 5, 36, 839968), null=True),
        ),
    ]
