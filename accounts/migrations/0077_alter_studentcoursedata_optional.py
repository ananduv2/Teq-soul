# Generated by Django 3.2.3 on 2021-09-15 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0076_alter_lead_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcoursedata',
            name='optional',
            field=models.CharField(choices=[('1', 'Yes'), ('0', 'No')], default='No', max_length=20, null=True),
        ),
    ]