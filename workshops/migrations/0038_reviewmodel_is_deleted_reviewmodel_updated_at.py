# Generated by Django 5.0.1 on 2024-02-20 07:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workshops", "0037_workshopmodel_updated_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="reviewmodel",
            name="is_deleted",
            field=models.BooleanField(
                default=False, help_text="Is deleted", verbose_name="is deleted"
            ),
        ),
        migrations.AddField(
            model_name="reviewmodel",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, help_text="Updated at", verbose_name="updated at"
            ),
        ),
    ]