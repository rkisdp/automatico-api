# Generated by Django 5.0.1 on 2024-01-31 01:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workshops", "0022_alter_reviewimagemodel_review"),
    ]

    operations = [
        migrations.AddField(
            model_name="reviewmodel",
            name="number",
            field=models.PositiveIntegerField(
                editable=False, help_text="Number", null=True, verbose_name="number"
            ),
        ),
    ]
