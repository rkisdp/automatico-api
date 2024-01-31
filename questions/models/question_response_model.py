from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from workshops.models import WorkshopModel

from .question_model import QuestionModel


class QuestionResponseModel(models.Model):
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
        related_name="question_responses",
        null=True,
        blank=True,
    )
    workshop = models.ForeignKey(
        verbose_name=_("workshop"),
        help_text=_("Workshop who the question was asked"),
        to=WorkshopModel,
        on_delete=models.PROTECT,
        related_name="question_responses",
        null=True,
        blank=True,
    )
    question = models.ForeignKey(
        verbose_name=_("question"),
        help_text=_("Question asked"),
        to=QuestionModel,
        on_delete=models.PROTECT,
        related_name="responses",
    )
    body = models.TextField(
        verbose_name=_("response"),
        help_text=_("Questioned at"),
        max_length=255,
    )
    created_at = models.DateTimeField(
        verbose_name=_("responded at"),
        help_text=_("Responded at"),
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        verbose_name = _("question response")
        verbose_name_plural = _("question responses")
        db_table = "question_response"

    def __str__(self) -> str:
        return f"{self.client} - {self.workshop}"
