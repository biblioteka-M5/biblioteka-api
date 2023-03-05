# Generated by Django 4.1.6 on 2023-03-05 13:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=150)),
                ("pages", models.PositiveSmallIntegerField()),
                ("is_available", models.BooleanField(default=True)),
                (
                    "genre",
                    models.CharField(
                        choices=[
                            ("Drama", "Drama"),
                            ("Romance", "Romance"),
                            ("Ficção", "Fiction"),
                            ("Não Ficção", "Non Fiction"),
                            ("Infantil", "Kids"),
                            ("Terror", "Horror"),
                            ("Suspense", "Triller"),
                            ("Ação e aventura", "Action Adventure"),
                        ],
                        max_length=30,
                    ),
                ),
                ("description", models.TextField()),
                ("published_at", models.PositiveSmallIntegerField()),
                ("author", models.CharField(max_length=100)),
                ("created_at", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
