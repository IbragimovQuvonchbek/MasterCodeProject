# Generated by Django 5.0.7 on 2024-07-12 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0003_remove_resultquestions_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultquestions',
            name='solution',
            field=models.TextField(default=None),
        ),
    ]
