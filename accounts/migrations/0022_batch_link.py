# Generated by Django 3.2.3 on 2021-07-16 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20210715_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]