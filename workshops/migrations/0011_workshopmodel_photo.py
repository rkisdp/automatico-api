# Generated by Django 4.2.7 on 2024-01-25 15:58

from django.db import migrations, models
import workshops.models.workshop_model


class Migration(migrations.Migration):
    dependencies = [
        ("workshops", "0010_alter_workshopmodel_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="workshopmodel",
            name="photo",
            field=models.ImageField(
                blank=True,
                help_text="The workshop photo.",
                null=True,
                upload_to=workshops.models.workshop_model.rename,
                verbose_name="photo",
            ),
        ),
    ]
