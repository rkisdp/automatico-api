from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from workshops.models import WorkshopModel

from .review_model import ReviewModel


class ReviewResponseModel(models.Model):
    id = models.AutoField(
        verbose_name=_("id"),
        help_text=_("Question id"),
        primary_key=True,
        unique=True,
        editable=False,
    )
    client = models.ForeignKey(
        verbose_name=_("client"),
        help_text=_("Client who asked the question"),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="review_responses",
        null=True,
        blank=True,
    )
    workshop = models.ForeignKey(
        verbose_name=_("workshop"),
        help_text=_("Workshop who the question was asked"),
        to=WorkshopModel,
        on_delete=models.PROTECT,
        related_name="review_responses",
        null=True,
        blank=True,
    )
    review = models.ForeignKey(
        verbose_name=_("review"),
        help_text=_("Review"),
        to=ReviewModel,
        on_delete=models.PROTECT,
        related_name="responses",
    )
    response = models.TextField(
        verbose_name=_("response"),
        help_text=_("reviewed at"),
        max_length=255,
    )
    responded_at = models.DateTimeField(
        verbose_name=_("responded at"),
        help_text=_("Responded at"),
        auto_now_add=True,
    )

    class Meta:
        verbose_name = _("review response")
        verbose_name_plural = _("review responses")
        db_table = "review_response"

    def __str__(self) -> str:
        return f"{self.client} - {self.workshop}"
