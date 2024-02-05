from django.db import models
from django.utils.translation import gettext_lazy as _

from .review_model import ReviewModel


class ReviewResponseModel(models.Model):
    id = models.AutoField(
        verbose_name=_("id"),
        help_text=_("Question id"),
        primary_key=True,
        unique=True,
        editable=False,
    )
    review = models.OneToOneField(
        verbose_name=_("review"),
        help_text=_("Review"),
        to=ReviewModel,
        on_delete=models.PROTECT,
        related_name="response",
        editable=False,
    )
    body = models.TextField(
        verbose_name=_("body"),
        help_text=_("Response body"),
        max_length=5000,
    )
    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        help_text=_("Response time"),
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        verbose_name = _("review response")
        verbose_name_plural = _("review responses")
        db_table = "review_response"

    def __str__(self) -> str:
        return f"#{self.review.number} - {self.review.workshop}"
