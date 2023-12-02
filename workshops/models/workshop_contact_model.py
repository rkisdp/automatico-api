from django.db import models
from django.utils.translation import gettext_lazy as _

from .workshop_model import WorkshopModel


class WorkshopContactModel(models.Model):
    id = models.AutoField(
        verbose_name=_("id"),
        help_text=_("Workshop contact id"),
        primary_key=True,
        unique=True,
        editable=False,
    )
    workshop = models.ForeignKey(
        verbose_name=_("workshop"),
        help_text=_("Workshop"),
        to=WorkshopModel,
        on_delete=models.PROTECT,
        related_name="workshops",
    )
    name = models.CharField(
        verbose_name=_("code"),
        help_text=_("Workshop code"),
        max_length=50,
        unique=True,
    )
    value = models.CharField(
        verbose_name=_("code"),
        help_text=_("Workshop code"),
        max_length=100,
        unique=True,
    )

    class Meta:
        verbose_name = _("workshop contact")
        verbose_name_plural = _("workshop contacts")
        db_table = "workshop_contact"

    def __str__(self) -> str:
        return self.name
