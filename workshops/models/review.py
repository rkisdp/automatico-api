from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_softdelete.models import SoftDeleteModel

from services.models import Service

from .workshop import Workshop


class Review(SoftDeleteModel):
    id = models.AutoField(
        verbose_name=_("id"),
        help_text=_("Review id"),
        primary_key=True,
        unique=True,
        editable=False,
    )
    workshop = models.ForeignKey(
        verbose_name=_("workshop"),
        help_text=_("Workshop"),
        to=Workshop,
        on_delete=models.PROTECT,
        related_name="reviews",
        null=True,
        blank=True,
    )
    service = models.ForeignKey(
        verbose_name=_("service"),
        help_text=_("Service"),
        to=Service,
        on_delete=models.PROTECT,
        related_name="reviews",
        null=True,
        blank=True,
    )
    client = models.ForeignKey(
        verbose_name=_("client"),
        help_text=_("Client"),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="reviews",
        null=True,
        blank=True,
    )
    number = models.PositiveIntegerField(
        verbose_name=_("number"),
        help_text=_("Number"),
        editable=False,
    )
    message = models.TextField(
        verbose_name=_("message"),
        help_text=_("Review message"),
        max_length=255,
    )
    rating = models.DecimalField(
        verbose_name=_("rating"),
        help_text=_("Rating"),
        max_digits=2,
        decimal_places=1,
        default=4,
        validators=(
            MinValueValidator(1.0),
            MaxValueValidator(5.0),
        ),
    )
    created_at = models.DateTimeField(
        verbose_name=_("responded at"),
        help_text=_("Responded at"),
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("updated at"),
        help_text=_("Updated at"),
        auto_now=True,
        editable=False,
    )

    class Meta:
        verbose_name = _("message")
        verbose_name_plural = _("reviews")
        db_table = "message"

    def __str__(self) -> str:
        return f"{self.client} - {self.workshop}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.number = self.workshop.reviews.count() + 1
        super().save(*args, **kwargs)
