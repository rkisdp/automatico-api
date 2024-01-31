from __future__ import annotations

from os import path
from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _

from .review_model import ReviewModel


def rename(instance: ReviewImageModel, filename: str) -> str:
    ext = filename.split(".")[-1]

    filename = f"{uuid4()}.{ext}"
    return path.join("workshops", "reviews", "images", filename)


class ReviewImageModel(models.Model):
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
        to=ReviewModel,
        on_delete=models.PROTECT,
        related_name="images",
    )
    image = models.ImageField(
        verbose_name=_("image"),
        help_text=_("Image"),
        upload_to=rename,
    )

    class Meta:
        verbose_name = _("review image")
        verbose_name_plural = _("review images")
        db_table = "review_image"

    def __str__(self) -> str:
        return f"{self.review} - {self.image}"
