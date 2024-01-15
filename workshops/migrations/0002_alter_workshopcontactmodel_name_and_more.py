# Generated by Django 4.2.7 on 2024-01-15 22:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workshops", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workshopcontactmodel",
            name="name",
            field=models.CharField(
                help_text="Workshop code", max_length=50, verbose_name="code"
            ),
        ),
        migrations.AlterField(
            model_name="workshopcontactmodel",
            name="value",
            field=models.CharField(
                help_text="Workshop code", max_length=100, verbose_name="code"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="workshopcontactmodel",
            unique_together={("workshop", "name")},
        ),
    ]
