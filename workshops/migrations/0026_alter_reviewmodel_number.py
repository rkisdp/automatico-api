# Generated by Django 5.0.1 on 2024-02-01 15:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workshops", "0025_alter_reviewresponsemodel_response"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reviewmodel",
            name="number",
            field=models.PositiveIntegerField(
                editable=False, help_text="Number", verbose_name="number"
            ),
        ),
    ]
