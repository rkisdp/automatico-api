from django.db import models
from django.utils.translation import gettext_lazy as _


class ServiceStatus(models.Model):
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

    class Meta:
        verbose_name = _("service status")
        verbose_name_plural = _("service statuses")
        db_table = "service status"

    def __str__(self) -> str:
        return self.name
