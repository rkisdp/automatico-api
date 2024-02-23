# Generated by Django 5.0.1 on 2024-02-23 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_rename_usermodel_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="deleted_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="restored_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]