# Generated by Django 4.2.7 on 2023-12-09 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("vehicles", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ServiceHistoryModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        editable=False,
                        help_text="Service id",
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="id",
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        help_text="Request description",
                        max_length=255,
                        verbose_name="request description",
                    ),
                ),
                (
                    "responsable",
                    models.TextField(
                        help_text="Response description",
                        max_length=255,
                        verbose_name="response description",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Start date",
                        verbose_name="start date",
                    ),
                ),
            ],
            options={
                "verbose_name": "service history",
                "verbose_name_plural": "service histories",
                "db_table": "service_history",
            },
        ),
        migrations.CreateModel(
            name="ServiceStatusModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        editable=False,
                        help_text="Vehicle brand id",
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="id",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Service status",
                        max_length=50,
                        unique=True,
                        verbose_name="service status",
                    ),
                ),
            ],
            options={
                "verbose_name": "service status",
                "verbose_name_plural": "service statuses",
                "db_table": "service status",
            },
        ),
        migrations.CreateModel(
            name="ServiceModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        editable=False,
                        help_text="Service id",
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="id",
                    ),
                ),
                (
                    "request_description",
                    models.TextField(
                        help_text="Request description",
                        max_length=255,
                        verbose_name="request description",
                    ),
                ),
                (
                    "response_description",
                    models.TextField(
                        help_text="Response description",
                        max_length=255,
                        verbose_name="response description",
                    ),
                ),
                (
                    "start_date",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Start date",
                        verbose_name="start date",
                    ),
                ),
                (
                    "end_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="End date",
                        null=True,
                        verbose_name="end date",
                    ),
                ),
                (
                    "vehicle",
                    models.ForeignKey(
                        help_text="Vehicle",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="services",
                        to="vehicles.vehiclemodel",
                        verbose_name="vehicle",
                    ),
                ),
            ],
            options={
                "verbose_name": "service",
                "verbose_name_plural": "services",
                "db_table": "service",
            },
        ),
    ]
