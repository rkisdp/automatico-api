# Generated by Django 5.0.1 on 2024-03-01 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("workshops", "0044_alter_workshop_description"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="message",
            new_name="body",
        ),
    ]
