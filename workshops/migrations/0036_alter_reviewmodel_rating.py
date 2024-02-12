# Generated by Django 5.0.1 on 2024-02-11 01:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workshops", "0035_alter_reviewmodel_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reviewmodel",
            name="rating",
            field=models.DecimalField(
                decimal_places=1,
                default=4,
                help_text="Rating",
                max_digits=2,
                validators=[
                    django.core.validators.MinValueValidator(1.0),
                    django.core.validators.MaxValueValidator(5.0),
                ],
                verbose_name="rating",
            ),
        ),
    ]
