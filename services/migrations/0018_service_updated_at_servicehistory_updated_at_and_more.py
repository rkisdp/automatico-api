# Generated by Django 5.0.1 on 2024-03-05 15:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0017_alter_service_vehicle_alter_service_workshop_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True,
                help_text="The date and time of last update.",
                verbose_name="updated at",
            ),
        ),
        migrations.AddField(
            model_name="servicehistory",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True,
                help_text="The date and time of last update.",
                verbose_name="updated at",
            ),
        ),
        migrations.AddField(
            model_name="servicestatus",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                help_text="The date and time of creation.",
                verbose_name="created at",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="servicestatus",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True,
                help_text="The date and time of last update.",
                verbose_name="updated at",
            ),
        ),
    ]