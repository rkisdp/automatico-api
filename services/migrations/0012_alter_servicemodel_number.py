# Generated by Django 5.0.1 on 2024-01-31 01:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("services", "0011_rename_end_date_servicemodel_closed_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servicemodel",
            name="number",
            field=models.PositiveIntegerField(
                editable=False,
                help_text="Workshop service number",
                null=True,
                verbose_name="workshop service number",
            ),
        ),
    ]
