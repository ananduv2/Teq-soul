# Generated by Django 3.2.5 on 2021-09-22 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0078_batch_batchcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batchcode',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
