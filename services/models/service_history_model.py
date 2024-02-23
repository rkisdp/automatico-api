from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from .service_model import Service
from .service_status_model import ServiceStatus


class ServiceHistory(models.Model):
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
        to=Service,
        on_delete=models.PROTECT,
        related_name="histories",
    )
    status = models.ForeignKey(
        verbose_name=_("status"),
        help_text=_("Status"),
        to=ServiceStatus,
        on_delete=models.PROTECT,
        related_name="histories",
    )
    comment = models.TextField(
        verbose_name=_("comment"),
        help_text=_("Comment"),
        max_length=255,
        null=True,
        blank=True,
    )
    responsable = models.ForeignKey(
        verbose_name=_("responsable"),
        help_text=_("Responsable"),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="service_histories",
    )
    created_at = models.DateTimeField(
        verbose_name=_("start date"),
        help_text=_("Start date"),
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        verbose_name = _("service history")
        verbose_name_plural = _("service histories")
        db_table = "service_history"

    def __str__(self) -> str:
        return f"{self.service} - {self.status}"
