# Generated by Django 5.0.1 on 2024-01-31 03:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("workshops", "0023_reviewmodel_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="workshopmodel",
            name="photo",
        ),
    ]
