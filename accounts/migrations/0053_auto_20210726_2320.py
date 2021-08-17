# Generated by Django 3.2.5 on 2021-07-26 17:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0052_auto_20210726_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcoursedata',
            name='optional',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=20),
        ),
        migrations.AlterField(
            model_name='query',
            name='datetime',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 7, 26, 23, 20, 36, 438631), null=True),
        ),
    ]