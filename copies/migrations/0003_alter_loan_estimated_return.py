# Generated by Django 4.1.7 on 2023-03-06 19:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("copies", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loan",
            name="estimated_return",
            field=models.DateField(default=datetime.date(2023, 4, 5)),
        ),
    ]
