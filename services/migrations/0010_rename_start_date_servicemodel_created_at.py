# Generated by Django 5.0.1 on 2024-01-30 14:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "services",
            "0009_rename_request_description_servicemodel_description_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="servicemodel",
            old_name="start_date",
            new_name="created_at",
        ),
    ]
