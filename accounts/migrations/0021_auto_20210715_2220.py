# Generated by Django 3.2.3 on 2021-07-15 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_alter_staff_blood_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='courses',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]