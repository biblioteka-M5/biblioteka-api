# Generated by Django 4.1.7 on 2023-03-15 20:53

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("copies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Loan",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("borrow_date", models.DateField(auto_now_add=True)),
                (
                    "estimated_return",
                    models.DateField(default=datetime.date(2023, 3, 30)),
                ),
                ("devolution_date", models.DateField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "copy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="copies_loans",
                        to="copies.copy",
                    ),
                ),
            ],
        ),
    ]
