# Generated by Django 5.0.1 on 2024-01-15 11:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0007_updates"),
    ]

    operations = [
        migrations.AddField(
            model_name="updates",
            name="slug",
            field=models.SlugField(blank=True),
        ),
    ]
