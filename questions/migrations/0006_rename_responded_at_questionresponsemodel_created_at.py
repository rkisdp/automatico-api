# Generated by Django 5.0.1 on 2024-01-31 03:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("questions", "0005_rename_message_questionmodel_body_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="questionresponsemodel",
            old_name="responded_at",
            new_name="created_at",
        ),
    ]