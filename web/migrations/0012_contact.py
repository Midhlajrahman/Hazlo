# Generated by Django 5.0.1 on 2024-01-15 12:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0011_testimonial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=300)),
                ("message", models.TextField()),
            ],
        ),
    ]