from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_softdelete.models import SoftDeleteModel

from .question import Question


class QuestionResponse(SoftDeleteModel):
    id = models.AutoField(
        verbose_name=_("id"),
        help_text=_("Question id"),
        primary_key=True,
        unique=True,
        editable=False,
    )
    body = models.TextField(
        verbose_name=_("response"),
        help_text=_("Questioned at"),
        max_length=1000,
    )
    votes = models.PositiveIntegerField(
        verbose_name=_("votes"),
        help_text=_("Number of votes"),
        default=0,
        editable=False,
    )
    user = models.ForeignKey(
        verbose_name=_("client"),
        help_text=_("Client who answered the question."),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="question_responses",
        editable=False,
    )
    question = models.ForeignKey(
        verbose_name=_("question"),
        help_text=_("Question asked"),
        to=Question,
        on_delete=models.PROTECT,
        related_name="answers",
        editable=False,
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
        verbose_name = _("question response")
        verbose_name_plural = _("question responses")
        db_table = "question_response"

    def __str__(self) -> str:
        return f"{self.question.number} - {self.question}"
