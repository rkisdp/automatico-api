# Generated by Django 5.0.1 on 2024-02-02 18:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("questions", "0013_questionmodel_votes_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="questionresponsemodel",
            name="votes",
            field=models.PositiveIntegerField(
                default=0,
                editable=False,
                help_text="Number of votes",
                verbose_name="votes",
            ),
        ),
    ]
