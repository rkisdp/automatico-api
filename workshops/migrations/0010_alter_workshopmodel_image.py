# Generated by Django 4.2.7 on 2024-01-25 15:53

from django.db import migrations, models
import workshops.models.workshop_model


class Migration(migrations.Migration):
    dependencies = [
        ("workshops", "0009_rename_photo_workshopmodel_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workshopmodel",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="The workshop image.",
                null=True,
                upload_to=workshops.models.workshop_model.rename,
                verbose_name="image",
            ),
        ),
    ]