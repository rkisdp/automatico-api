# Generated by Django 5.0.1 on 2024-02-22 23:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "questions",
            "0015_questionmodel_is_deleted_questionmodel_updated_at_and_more",
        ),
        ("workshops", "0040_workshopmodel_banner"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="QuestionModel",
            new_name="Question",
        ),
        migrations.RenameModel(
            old_name="QuestionResponseModel",
            new_name="QuestionResponse",
        ),
    ]
