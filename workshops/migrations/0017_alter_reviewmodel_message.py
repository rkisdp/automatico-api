# Generated by Django 5.0.1 on 2024-01-30 15:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workshops", "0016_alter_reviewmodel_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reviewmodel",
            name="message",
            field=models.TextField(
                help_text="Review message", max_length=255, verbose_name="message"
            ),
        ),
    ]
