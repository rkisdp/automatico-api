# Generated by Django 4.2.7 on 2024-01-17 16:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vehicles", "0002_alter_vehiclemodel_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="vehiclemodel",
            name="plate",
            field=models.CharField(
                default="", help_text="Plate", max_length=7, verbose_name="plate"
            ),
            preserve_default=False,
        ),
    ]