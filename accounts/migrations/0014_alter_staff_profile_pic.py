# Generated by Django 3.2.3 on 2021-07-14 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_staff_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='profile_pic',
            field=models.ImageField(blank=True, default='user-circle-solid.jpg', null=True, upload_to=''),
        ),
    ]
