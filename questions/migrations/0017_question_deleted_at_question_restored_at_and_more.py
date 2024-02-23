# Generated by Django 5.0.1 on 2024-02-23 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0016_rename_questionmodel_question_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="deleted_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="question",
            name="restored_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="questionresponse",
            name="deleted_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="questionresponse",
            name="restored_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]