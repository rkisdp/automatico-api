# Generated by Django 5.0.1 on 2024-02-04 23:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workshops", "0029_remove_reviewresponsemodel_client_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reviewresponsemodel",
            name="review",
            field=models.OneToOneField(
                help_text="Review",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="response",
                to="workshops.reviewmodel",
                verbose_name="review",
            ),
        ),
    ]
