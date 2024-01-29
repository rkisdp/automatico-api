# Generated by Django 5.0.1 on 2024-01-29 17:39

import django.core.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vehicles", "0006_vehiclebrandmodel_image"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehiclemodel",
            name="year",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Year",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1900),
                    django.core.validators.MaxValueValidator(2100),
                ],
                verbose_name="year",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="vehiclemodel",
            unique_together={
                ("nickname", "owner"),
                ("plate", "owner"),
                ("vin", "owner"),
            },
        ),
    ]
