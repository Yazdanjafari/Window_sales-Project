# Generated by Django 5.0.2 on 2024-07-17 13:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Measurement_App', '0002_measurementform_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurementform',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
