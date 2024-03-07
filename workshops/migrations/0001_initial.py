# Generated by Django 4.2.7 on 2023-12-09 17:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import reviews.models.review_image
import workshops.models.workshop


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("vehicles", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="QuestionModel",
            fields=[
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
                    "question",
                    models.CharField(
                        help_text="Workshop code",
                        max_length=50,
                        unique=True,
                        verbose_name="code",
                    ),
                ),
                (
                    "questioned_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Questioned at",
                        verbose_name="questioned at",
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        help_text="Client who asked the question",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="questions",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="client",
                    ),
                ),
            ],
            options={
                "verbose_name": "question",
                "verbose_name_plural": "questions",
                "db_table": "question",
            },
        ),
        migrations.CreateModel(
            name="ReviewModel",
            fields=[
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
                    "review",
                    models.TextField(
                        help_text="Reviewed at",
                        max_length=255,
                        verbose_name="review",
                    ),
                ),
                (
                    "qualification",
                    models.TextField(
                        help_text="Questioned at",
                        max_length=255,
                        verbose_name="response",
                    ),
                ),
                (
                    "reviewed_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Responded at",
                        verbose_name="responded at",
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        blank=True,
                        help_text="Client",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
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
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="reviews",
                        to="services.servicemodel",
                        verbose_name="service",
                    ),
                ),
            ],
            options={
                "verbose_name": "review",
                "verbose_name_plural": "reviews",
                "db_table": "review",
            },
        ),
        migrations.CreateModel(
            name="SpecialityModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        editable=False,
                        help_text="Speciality id",
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="id",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Workshop speciality",
                        max_length=50,
                        unique=True,
                        verbose_name="speciality",
                    ),
                ),
            ],
            options={
                "verbose_name": "speciality",
                "verbose_name_plural": "specialities",
                "db_table": "speciality",
            },
        ),
        migrations.CreateModel(
            name="WorkshopModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        editable=False,
                        help_text="Workshop id",
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="id",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Workshop name",
                        max_length=100,
                        unique=True,
                        verbose_name="name",
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        help_text="Workshop photo",
                        null=True,
                        upload_to=workshops.models.workshop.rename,
                        verbose_name="photo",
                    ),
                ),
                (
                    "latitude",
                    models.DecimalField(
                        blank=True,
                        decimal_places=6,
                        help_text="Workshop latitude",
                        max_digits=9,
                        null=True,
                        verbose_name="latitude",
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(
                        blank=True,
                        decimal_places=6,
                        help_text="Workshop longitude",
                        max_digits=9,
                        null=True,
                        verbose_name="longitude",
                    ),
                ),
                (
                    "employees",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Workshop employees",
                        related_name="workshop_empoyees",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="employees",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        help_text="Owner",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="workshops",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="owner",
                    ),
                ),
                (
                    "specialities",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Workshop specialities",
                        related_name="workshop_specialities",
                        to="workshops.specialitymodel",
                        verbose_name="specialities",
                    ),
                ),
                (
                    "vehicles",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Workshop vehicles",
                        related_name="workshop_vehicles",
                        to="vehicles.vehiclemodel",
                        verbose_name="vehicles",
                    ),
                ),
            ],
            options={
                "verbose_name": "workshop",
                "verbose_name_plural": "workshops",
                "db_table": "workshop",
            },
        ),
        migrations.CreateModel(
            name="WorkshopContactModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        editable=False,
                        help_text="Workshop contact id",
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="id",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Workshop code",
                        max_length=50,
                        unique=True,
                        verbose_name="code",
                    ),
                ),
                (
                    "value",
                    models.CharField(
                        help_text="Workshop code",
                        max_length=100,
                        unique=True,
                        verbose_name="code",
                    ),
                ),
                (
                    "workshop",
                    models.ForeignKey(
                        help_text="Workshop",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="workshops",
                        to="workshops.workshopmodel",
                        verbose_name="workshop",
                    ),
                ),
            ],
            options={
                "verbose_name": "workshop contact",
                "verbose_name_plural": "workshop contacts",
                "db_table": "workshop_contact",
            },
        ),
        migrations.CreateModel(
            name="ReviewResponseModel",
            fields=[
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
                    "response",
                    models.TextField(
                        help_text="reviewed at",
                        max_length=255,
                        verbose_name="response",
                    ),
                ),
                (
                    "responded_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Responded at",
                        verbose_name="responded at",
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        blank=True,
                        help_text="Client who asked the question",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="review_responses",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="client",
                    ),
                ),
                (
                    "review",
                    models.ForeignKey(
                        help_text="Review",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="responses",
                        to="workshops.reviewmodel",
                        verbose_name="review",
                    ),
                ),
                (
                    "workshop",
                    models.ForeignKey(
                        blank=True,
                        help_text="Workshop who the question was asked",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="review_responses",
                        to="workshops.workshopmodel",
                        verbose_name="workshop",
                    ),
                ),
            ],
            options={
                "verbose_name": "review response",
                "verbose_name_plural": "review responses",
                "db_table": "review_response",
            },
        ),
        migrations.CreateModel(
            name="ReviewPhotoModel",
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
                    "photo",
                    models.ImageField(
                        help_text="Photo",
                        upload_to=reviews.models.review_image.rename,
                        verbose_name="photo",
                    ),
                ),
                (
                    "review",
                    models.ForeignKey(
                        help_text="Review",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="reviews",
                        to="workshops.reviewmodel",
                        verbose_name="review",
                    ),
                ),
            ],
            options={
                "verbose_name": "review photo",
                "verbose_name_plural": "review photos",
                "db_table": "review_photo",
            },
        ),
        migrations.AddField(
            model_name="reviewmodel",
            name="workshop",
            field=models.ForeignKey(
                blank=True,
                help_text="Workshop",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="reviews",
                to="workshops.workshopmodel",
                verbose_name="workshop",
            ),
        ),
        migrations.CreateModel(
            name="QuestionResponseModel",
            fields=[
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
                    "response",
                    models.TextField(
                        help_text="Questioned at",
                        max_length=255,
                        verbose_name="response",
                    ),
                ),
                (
                    "responded_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Responded at",
                        verbose_name="responded at",
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        blank=True,
                        help_text="Client who asked the question",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="question_responses",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="client",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        help_text="Question asked",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="responses",
                        to="workshops.questionmodel",
                        verbose_name="question",
                    ),
                ),
                (
                    "workshop",
                    models.ForeignKey(
                        blank=True,
                        help_text="Workshop who the question was asked",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="question_responses",
                        to="workshops.workshopmodel",
                        verbose_name="workshop",
                    ),
                ),
            ],
            options={
                "verbose_name": "question response",
                "verbose_name_plural": "question responses",
                "db_table": "question_response",
            },
        ),
        migrations.AddField(
            model_name="questionmodel",
            name="workshop",
            field=models.ForeignKey(
                help_text="Workshop who the question was asked",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="questions",
                to="workshops.workshopmodel",
                verbose_name="workshop",
            ),
        ),
    ]
