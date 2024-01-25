from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from services.models import ServiceModel
from workshops.models import WorkshopModel


class ReviewModel(models.Model):
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
        to=WorkshopModel,
        on_delete=models.PROTECT,
        related_name="reviews",
        null=True,
        blank=True,
    )
    service = models.ForeignKey(
        verbose_name=_("service"),
        help_text=_("Service"),
        to=ServiceModel,
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
    review = models.TextField(
        verbose_name=_("review"),
        help_text=_("Review message"),
        max_length=255,
    )
    score = models.DecimalField(
        verbose_name=_("score"),
        help_text=_("Score"),
        max_digits=2,
        decimal_places=1,
        default=4.5,
    )
    reviewed_at = models.DateTimeField(
        verbose_name=_("responded at"),
        help_text=_("Responded at"),
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        verbose_name = _("review")
        verbose_name_plural = _("reviews")
        db_table = "review"

    def __str__(self) -> str:
        return f"{self.client} - {self.workshop}"