# Generated by Django 5.0.1 on 2024-03-06 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("security", "0011_verificationcode_deleted_at_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="verificationcode",
            name="deleted_at",
        ),
        migrations.RemoveField(
            model_name="verificationcode",
            name="restored_at",
        ),
    ]
