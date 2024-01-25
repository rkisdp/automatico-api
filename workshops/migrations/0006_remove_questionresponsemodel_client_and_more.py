# Generated by Django 4.2.7 on 2024-01-23 07:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "workshops",
            "0005_remove_reviewmodel_qualification_reviewmodel_score_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="questionresponsemodel",
            name="client",
        ),
        migrations.RemoveField(
            model_name="questionresponsemodel",
            name="question",
        ),
        migrations.RemoveField(
            model_name="questionresponsemodel",
            name="workshop",
        ),
        migrations.DeleteModel(
            name="QuestionModel",
        ),
        migrations.DeleteModel(
            name="QuestionResponseModel",
        ),
    ]
