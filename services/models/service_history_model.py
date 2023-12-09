from django.db import models
from django.utils.translation import gettext_lazy as _

from .service_model import ServiceModel
from .service_status_model import ServiceStatusModel


class ServiceHistoryModel(models.Model):
    id = models.AutoField(
        verbose_name=_("id"),
        help_text=_("Service id"),
        primary_key=True,
        unique=True,
        editable=False,
    )
    service = models.ForeignKey(
        verbose_name=_("service"),
        help_text=_("Service"),
        to=ServiceModel,
        on_delete=models.PROTECT,
        related_name="histories",
    )
    status = models.ForeignKey(
        verbose_name=_("status"),
        help_text=_("Status"),
        to=ServiceStatusModel,
        on_delete=models.PROTECT,
        related_name="histories",
    )
    comment = models.TextField(
        verbose_name=_("request description"),
        help_text=_("Request description"),
        max_length=255,
    )
    responsable = models.TextField(
        verbose_name=_("response description"),
        help_text=_("Response description"),
        max_length=255,
    )
    created_at = models.DateTimeField(
        verbose_name=_("start date"),
        help_text=_("Start date"),
        auto_now_add=True,
    )

    class Meta:
        verbose_name = _("service history")
        verbose_name_plural = _("service histories")
        db_table = "service_history"

    def __str__(self) -> str:
        return f"{self.service} - {self.status}"
