# Generated by Django 5.0.1 on 2024-02-23 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("vehicles", "0019_vehicle_deleted_at_vehicle_restored_at_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vehicle",
            name="is_deleted",
        ),
    ]
