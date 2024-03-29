# Generated by Django 5.0.1 on 2024-03-05 14:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0018_remove_question_is_deleted_and_more"),
        ("workshops", "0046_alter_review_body"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="user",
            field=models.ForeignKey(
                editable=False,
                help_text="Client who asked the question",
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="questions",
                to=settings.AUTH_USER_MODEL,
                verbose_name="client",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="workshop",
            field=models.ForeignKey(
                editable=False,
                help_text="Workshop who the question was asked",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="workshops.workshop",
                verbose_name="workshop",
            ),
        ),
        migrations.AlterField(
            model_name="questionresponse",
            name="user",
            field=models.ForeignKey(
                editable=False,
                help_text="Client who answered the question.",
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="question_responses",
                to=settings.AUTH_USER_MODEL,
                verbose_name="client",
            ),
        ),
    ]
