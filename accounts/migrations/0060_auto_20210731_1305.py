# Generated by Django 3.2.5 on 2021-07-31 07:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0059_auto_20210731_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='batch',
            field=models.ForeignKey(blank=True, limit_choices_to={'status': 'Ongoing'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.batch'),
        ),
        migrations.AlterField(
            model_name='query',
            name='datetime',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 7, 31, 13, 5, 23, 172426), null=True),
        ),
    ]