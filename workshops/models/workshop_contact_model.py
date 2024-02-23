from django.db import models
from django.utils.translation import gettext_lazy as _

from .workshop_model import Workshop


class WorkshopContact(models.Model):
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
        to=Workshop,
        on_delete=models.PROTECT,
        related_name="contacts",
    )
    name = models.CharField(
        verbose_name=_("code"),
        help_text=_("Workshop code"),
        max_length=50,
    )
    value = models.CharField(
        verbose_name=_("code"),
        help_text=_("Workshop code"),
        max_length=100,
    )

    class Meta:
        verbose_name = _("workshop contact")
        verbose_name_plural = _("workshop contacts")
        db_table = "workshop_contact"
        unique_together = ("workshop", "name")

    def __str__(self) -> str:
        return self.name
