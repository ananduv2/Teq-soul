# Generated by Django 3.2.3 on 2021-07-12 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_batch_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='status',
            field=models.CharField(choices=[('Yet to start', 'Yet to start'), ('Yet to start', 'Ongoing'), ('Yet to start', 'Completed')], default=1, max_length=100),
        ),
        migrations.AlterField(
            model_name='batch',
            name='trainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.staff'),
        ),
    ]
