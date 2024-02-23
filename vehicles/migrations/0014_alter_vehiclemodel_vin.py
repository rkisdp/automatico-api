# Generated by Django 5.0.1 on 2024-02-20 06:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vehicles", "0013_vehiclemodel_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehiclemodel",
            name="vin",
            field=models.CharField(
                blank=True,
                help_text="VIN",
                max_length=17,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="VIN must be 17 characters long.",
                        regex="^[A-HJ-NPR-Z\\d]{8}[\\dX][A-HJ-NPR-Z\\d]{2}\\d{6}$",
                    )
                ],
                verbose_name="vin",
            ),
        ),
    ]