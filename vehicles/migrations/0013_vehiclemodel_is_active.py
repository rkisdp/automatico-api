# Generated by Django 5.0.1 on 2024-02-20 06:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vehicles", "0012_alter_vehiclemodel_plate_alter_vehiclemodel_vin"),
    ]

    operations = [
        migrations.AddField(
            model_name="vehiclemodel",
            name="is_active",
            field=models.BooleanField(
                default=True, help_text="Active", verbose_name="active"
            ),
        ),
    ]
