from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from workshops.models import Workshop


class Question(models.Model):
    id = models.AutoField(
        verbose_name=_("id"),
        help_text=_("The unique identifier of the question."),
        primary_key=True,
        unique=True,
        editable=False,
    )
    number = models.PositiveIntegerField(
        verbose_name=_("number"),
        help_text=_("Question number"),
        editable=False,
    )
    body = models.CharField(
        verbose_name=_("question"),
        help_text=_("Question asked by the client"),
        max_length=200,
    )
    votes = models.PositiveIntegerField(
        verbose_name=_("votes"),
        help_text=_("Number of votes"),
        default=0,
        editable=False,
    )
    user = models.ForeignKey(
        verbose_name=_("client"),
        help_text=_("Client who asked the question"),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="questions",
        editable=False,
    )
    workshop = models.ForeignKey(
        verbose_name=_("workshop"),
        help_text=_("Workshop who the question was asked"),
        to=Workshop,
        on_delete=models.PROTECT,
        related_name="questions",
        editable=False,
    )
    is_deleted = models.BooleanField(
        verbose_name=_("is deleted"),
        help_text=_("Indicates if the question is deleted"),
        default=False,
        editable=False,
    )
    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        help_text=_("Created at"),
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
        verbose_name = _("question")
        verbose_name_plural = _("questions")
        db_table = "question"

    def __str__(self) -> str:
        return f"{self.body} #{self.number} - {self.workshop}"

    def save(self, *args, **kwargs):
        if not self.number:
            self.number = self.workshop.questions.count() + 1
        super().save(*args, **kwargs)

    @property
    def answer(self):
        return self.answers.order_by("votes", "-created_at").first()
