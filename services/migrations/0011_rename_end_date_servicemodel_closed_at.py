# Generated by Django 5.0.1 on 2024-01-30 14:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("services", "0010_rename_start_date_servicemodel_created_at"),
    ]

    operations = [
        migrations.RenameField(
            model_name="servicemodel",
            old_name="end_date",
            new_name="closed_at",
        ),
    ]