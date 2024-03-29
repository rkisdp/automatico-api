# Generated by Django 5.0.1 on 2024-02-04 23:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workshops", "0028_rename_response_reviewresponsemodel_body_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reviewresponsemodel",
            name="client",
        ),
        migrations.AlterField(
            model_name="reviewresponsemodel",
            name="body",
            field=models.TextField(
                help_text="Response body", max_length=5000, verbose_name="body"
            ),
        ),
        migrations.AlterField(
            model_name="reviewresponsemodel",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, help_text="Response time", verbose_name="created at"
            ),
        ),
    ]
