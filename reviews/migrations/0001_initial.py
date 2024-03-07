# Generated by Django 5.0.1 on 2024-03-07 13:48

import django.core.validators
import django.db.models.deletion
import reviews.models.review_image
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        (
            "services",
            "0018_service_updated_at_servicehistory_updated_at_and_more",
        ),
        (
            "workshops",
            "0050_remove_review_client_remove_review_service_and_more",
        ),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name="Review",
                    fields=[
                        (
                            "deleted_at",
                            models.DateTimeField(blank=True, null=True),
                        ),
                        (
                            "restored_at",
                            models.DateTimeField(blank=True, null=True),
                        ),
                        (
                            "id",
                            models.AutoField(
                                editable=False,
                                help_text="Review id",
                                primary_key=True,
                                serialize=False,
                                unique=True,
                                verbose_name="id",
                            ),
                        ),
                        (
                            "number",
                            models.PositiveIntegerField(
                                editable=False,
                                help_text="Number",
                                verbose_name="number",
                            ),
                        ),
                        (
                            "body",
                            models.TextField(
                                help_text="Review body",
                                max_length=255,
                                verbose_name="body",
                            ),
                        ),
                        (
                            "rating",
                            models.DecimalField(
                                decimal_places=1,
                                default=4,
                                help_text="Rating",
                                max_digits=2,
                                validators=[
                                    django.core.validators.MinValueValidator(
                                        1.0
                                    ),
                                    django.core.validators.MaxValueValidator(
                                        5.0
                                    ),
                                ],
                                verbose_name="rating",
                            ),
                        ),
                        (
                            "created_at",
                            models.DateTimeField(
                                auto_now_add=True,
                                help_text="Responded at",
                                verbose_name="responded at",
                            ),
                        ),
                        (
                            "updated_at",
                            models.DateTimeField(
                                auto_now=True,
                                help_text="Updated at",
                                verbose_name="updated at",
                            ),
                        ),
                        (
                            "client",
                            models.ForeignKey(
                                blank=True,
                                help_text="Client",
                                null=True,
                                on_delete=django.db.models.deletion.CASCADE,
                                related_name="reviews",
                                to=settings.AUTH_USER_MODEL,
                                verbose_name="client",
                            ),
                        ),
                        (
                            "service",
                            models.ForeignKey(
                                blank=True,
                                help_text="Service",
                                null=True,
                                on_delete=django.db.models.deletion.DO_NOTHING,
                                related_name="reviews",
                                to="services.service",
                                verbose_name="service",
                            ),
                        ),
                        (
                            "workshop",
                            models.ForeignKey(
                                blank=True,
                                help_text="Workshop",
                                null=True,
                                on_delete=django.db.models.deletion.CASCADE,
                                related_name="reviews",
                                to="workshops.workshop",
                                verbose_name="workshop",
                            ),
                        ),
                    ],
                    options={
                        "verbose_name": "message",
                        "verbose_name_plural": "reviews",
                        "db_table": "message",
                    },
                ),
                migrations.CreateModel(
                    name="ReviewImage",
                    fields=[
                        (
                            "deleted_at",
                            models.DateTimeField(blank=True, null=True),
                        ),
                        (
                            "restored_at",
                            models.DateTimeField(blank=True, null=True),
                        ),
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
                            "image",
                            models.ImageField(
                                help_text="Image",
                                upload_to=reviews.models.review_image.rename,
                                verbose_name="image",
                            ),
                        ),
                        (
                            "created_at",
                            models.DateTimeField(
                                auto_now_add=True,
                                help_text="The date and time of creation.",
                                verbose_name="created at",
                            ),
                        ),
                        (
                            "updated_at",
                            models.DateTimeField(
                                auto_now=True,
                                help_text="The date and time of last update.",
                                verbose_name="updated at",
                            ),
                        ),
                        (
                            "review",
                            models.ForeignKey(
                                help_text="Review",
                                on_delete=django.db.models.deletion.CASCADE,
                                related_name="images",
                                to="reviews.review",
                                verbose_name="review",
                            ),
                        ),
                    ],
                    options={
                        "verbose_name": "review image",
                        "verbose_name_plural": "review images",
                        "db_table": "review_image",
                    },
                ),
                migrations.CreateModel(
                    name="ReviewResponse",
                    fields=[
                        (
                            "deleted_at",
                            models.DateTimeField(blank=True, null=True),
                        ),
                        (
                            "restored_at",
                            models.DateTimeField(blank=True, null=True),
                        ),
                        (
                            "id",
                            models.AutoField(
                                editable=False,
                                help_text="Question id",
                                primary_key=True,
                                serialize=False,
                                unique=True,
                                verbose_name="id",
                            ),
                        ),
                        (
                            "body",
                            models.TextField(
                                help_text="Response body",
                                max_length=5000,
                                verbose_name="body",
                            ),
                        ),
                        (
                            "created_at",
                            models.DateTimeField(
                                auto_now_add=True,
                                help_text="The date and time of creation.",
                                verbose_name="created at",
                            ),
                        ),
                        (
                            "updated_at",
                            models.DateTimeField(
                                auto_now=True,
                                help_text="The date and time of last update.",
                                verbose_name="updated at",
                            ),
                        ),
                        (
                            "review",
                            models.OneToOneField(
                                editable=False,
                                help_text="Review",
                                on_delete=django.db.models.deletion.PROTECT,
                                related_name="response",
                                to="reviews.review",
                                verbose_name="review",
                            ),
                        ),
                    ],
                    options={
                        "verbose_name": "review response",
                        "verbose_name_plural": "review responses",
                        "db_table": "review_response",
                    },
                ),
            ],
            database_operations=[],
        )
    ]