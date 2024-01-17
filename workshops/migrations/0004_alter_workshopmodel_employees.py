# Generated by Django 4.2.7 on 2024-01-17 20:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("workshops", "0003_workshopmodel_brands"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workshopmodel",
            name="employees",
            field=models.ManyToManyField(
                blank=True,
                help_text="Workshop employees",
                related_name="workshop_employees",
                to=settings.AUTH_USER_MODEL,
                verbose_name="employees",
            ),
        ),
    ]
