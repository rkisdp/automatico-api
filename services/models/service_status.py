from django.db import models
from django.utils.translation import gettext_lazy as _
from django_softdelete.models import SoftDeleteModel


class ServiceStatus(SoftDeleteModel):
    id = models.AutoField(
        verbose_name=_("id"),
        help_text=_("Vehicle brand id"),
        primary_key=True,
        unique=True,
        editable=False,
    )
    name = models.CharField(
        verbose_name=_("service status"),
        help_text=_("Service status"),
        max_length=50,
        unique=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        help_text=_("The date and time of creation."),
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("updated at"),
        help_text=_("The date and time of last update."),
        auto_now=True,
        editable=False,
    )

    class Meta:
        verbose_name = _("service status")
        verbose_name_plural = _("service statuses")
        db_table = "service status"

    def __str__(self) -> str:
        return self.name
