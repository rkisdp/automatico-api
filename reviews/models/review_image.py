from __future__ import annotations

from os import path
from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_softdelete.models import SoftDeleteModel

from .review import Review


def rename(instance: ReviewImage, filename: str) -> str:
    ext = filename.split(".")[-1]

    filename = f"{uuid4()}.{ext}"
    return path.join("workshops", "reviews", "images", filename)


class ReviewImage(SoftDeleteModel):
    id = models.AutoField(
        verbose_name=_("id"),
        help_text=_("Vehicle brand id"),
        primary_key=True,
        unique=True,
        editable=False,
    )
    review = models.ForeignKey(
        verbose_name=_("review"),
        help_text=_("Review"),
        to=Review,
        on_delete=models.CASCADE,
        related_name="images",
    )
    image = models.ImageField(
        verbose_name=_("image"),
        help_text=_("Image"),
        upload_to=rename,
    )
    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        help_text=_("The date and time of creation."),
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("updated at"),
        help_text=_("The date and time of last update."),
        auto_now=True,
        editable=False,
    )

    class Meta:
        verbose_name = _("review image")
        verbose_name_plural = _("review images")
        db_table = "review_image"

    def __str__(self) -> str:
        return f"{self.review} - {self.image}"
