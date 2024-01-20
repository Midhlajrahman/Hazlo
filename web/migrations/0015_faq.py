# Generated by Django 4.2.5 on 2024-01-18 06:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0014_remove_productimages_name_updates_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="Faq",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
            ],
        ),
    ]