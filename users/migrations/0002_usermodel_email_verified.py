# Generated by Django 4.2.7 on 2024-01-06 13:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="usermodel",
            name="email_verified",
            field=models.BooleanField(
                default=False,
                help_text="User email verification status",
                verbose_name="email verified",
            ),
        ),
    ]