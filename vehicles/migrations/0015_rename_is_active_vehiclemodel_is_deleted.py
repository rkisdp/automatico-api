# Generated by Django 5.0.1 on 2024-02-20 06:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("vehicles", "0014_alter_vehiclemodel_vin"),
    ]

    operations = [
        migrations.RenameField(
            model_name="vehiclemodel",
            old_name="is_active",
            new_name="is_deleted",
        ),
    ]
