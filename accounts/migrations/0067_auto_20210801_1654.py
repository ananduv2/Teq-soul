# Generated by Django 3.2.5 on 2021-08-01 11:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0066_auto_20210801_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='datetime',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 8, 1, 16, 54, 51, 669739), null=True),
        ),
        migrations.AlterField(
            model_name='studentprojectdata',
            name='submitted_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]