# Generated by Django 5.0.1 on 2024-02-04 22:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vehicles", "0009_vehiclemodel_archived"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehiclemodel",
            name="plate",
            field=models.CharField(
                blank=True,
                help_text="Plate",
                max_length=8,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Plate must be in the format 'A000000'.",
                        regex="^(A{1,2}|B|C|D|F|G|L|H|I|T|P|U|J|R|S|M|OE|OF|OM|OP|E[AGLMEID]|VC|WD|OI|EX|YX|Z|NZ|DD|PP|K)-\\d{1,6}$",
                    )
                ],
                verbose_name="plate",
            ),
        ),
    ]
