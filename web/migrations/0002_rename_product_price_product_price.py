# Generated by Django 5.0.1 on 2024-01-15 10:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="product_price",
            new_name="price",
        ),
    ]