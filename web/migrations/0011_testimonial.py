# Generated by Django 5.0.1 on 2024-01-15 12:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0010_alter_updates_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="Testimonial",
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
                ("image", models.ImageField(upload_to="testimonial/")),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("name", models.CharField(blank=True, max_length=100)),
                ("position", models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
