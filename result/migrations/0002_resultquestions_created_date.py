# Generated by Django 5.0.7 on 2024-07-12 15:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultquestions',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 12, 15, 3, 59, 953644)),
        ),
    ]
