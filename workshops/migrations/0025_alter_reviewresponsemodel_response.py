# Generated by Django 5.0.1 on 2024-01-31 05:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workshops", "0024_remove_workshopmodel_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reviewresponsemodel",
            name="response",
            field=models.TextField(
                help_text="reviewed at", max_length=5000, verbose_name="response"
            ),
        ),
    ]
