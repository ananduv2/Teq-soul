# Generated by Django 3.2.5 on 2021-08-09 16:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0072_alter_query_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doubt',
            name='ss1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='doubt',
            name='ss2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='doubt',
            name='ss3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='query',
            name='datetime',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 8, 9, 21, 49, 28, 418008), null=True),
        ),
    ]