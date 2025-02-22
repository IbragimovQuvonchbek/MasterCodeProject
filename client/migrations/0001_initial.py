# Generated by Django 5.0.7 on 2024-07-12 15:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('created_date', models.DateField(default=datetime.date(2024, 7, 12))),
            ],
        ),
    ]
