# Generated by Django 4.2.7 on 2024-01-25 15:40

from django.db import migrations, models
import vehicles.models.vehicle_brand


class Migration(migrations.Migration):
    dependencies = [
        ("vehicles", "0005_remove_vehiclemodel_photo_vehiclemodel_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="vehiclebrandmodel",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="Image",
                null=True,
                upload_to=vehicles.models.vehicle_brand.rename,
                verbose_name="image",
            ),
        ),
    ]
