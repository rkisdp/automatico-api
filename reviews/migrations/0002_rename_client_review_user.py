# Generated by Django 5.0.1 on 2024-03-07 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="client",
            new_name="user",
        ),
    ]
