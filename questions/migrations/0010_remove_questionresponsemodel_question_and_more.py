# Generated by Django 5.0.1 on 2024-02-01 02:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("questions", "0009_rename_client_questionmodel_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="questionresponsemodel",
            name="question",
        ),
        migrations.AddField(
            model_name="questionresponsemodel",
            name="questions",
            field=models.ForeignKey(
                default=1,
                editable=False,
                help_text="Question asked",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="responses",
                to="questions.questionmodel",
                verbose_name="question",
            ),
            preserve_default=False,
        ),
    ]
