from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from workshops.models import WorkshopModel


class QuestionModel(models.Model):
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
        related_name="questions",
    )
    workshop = models.ForeignKey(
        verbose_name=_("workshop"),
        help_text=_("Workshop who the question was asked"),
        to=WorkshopModel,
        on_delete=models.PROTECT,
        related_name="questions",
    )
    question = models.CharField(
        verbose_name=_("question"),
        help_text=_("Question asked by the client"),
        max_length=50,
    )
    questioned_at = models.DateTimeField(
        verbose_name=_("questioned at"),
        help_text=_("Questioned at"),
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        verbose_name = _("question")
        verbose_name_plural = _("questions")
        db_table = "question"

    def __str__(self) -> str:
        return f"{self.client} - {self.workshop}"
