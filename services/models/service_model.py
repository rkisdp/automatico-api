from django.db import models
from django.utils.translation import gettext_lazy as _

from vehicles.models import VehicleModel

# from workshops.models import WorkshopModel


class ServiceModel(models.Model):
    id = models.AutoField(
        verbose_name=_("id"),
        help_text=_("Service id"),
        primary_key=True,
        unique=True,
        editable=False,
    )
    vehicle = models.ForeignKey(
        verbose_name=_("vehicle"),
        help_text=_("Vehicle"),
        to=VehicleModel,
        on_delete=models.PROTECT,
        related_name="services",
    )
    workshop = models.ForeignKey(
        verbose_name=_("workshop"),
        help_text=_("Workshop"),
        to="workshops.WorkshopModel",
        on_delete=models.PROTECT,
        related_name="services",
    )
    number = models.IntegerField(
        verbose_name=_("workshop service number"),
        help_text=_("Workshop service number"),
        editable=False,
        null=True,
    )
    title = models.CharField(
        verbose_name=_("title"),
        help_text=_("Service title"),
        max_length=100,
        null=True,
    )
    description = models.TextField(
        verbose_name=_("request description"),
        help_text=_("Request description"),
        max_length=255,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_("start date"),
        help_text=_("Start date"),
        auto_now_add=True,
        editable=False,
    )
    closed_at = models.DateTimeField(
        verbose_name=_("end date"),
        help_text=_("End date"),
        null=True,
        blank=True,
        editable=False,
    )

    class Meta:
        verbose_name = _("service")
        verbose_name_plural = _("services")
        unique_together = ("workshop", "number")
        db_table = "service"

    def __str__(self) -> str:
        return f"{self.vehicle} - {self.workshop}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.number = self.workshop.services.count() + 1
        super().save(*args, **kwargs)

    @property
    def current_status(self) -> str | None:
        return (
            self.histories.last().status.name if self.histories.last() else None
        )

    @property
    def current_status_id(self) -> int | None:
        return (
            self.histories.last().status.id if self.histories.last() else None
        )

    @property
    def requested_by(self) -> str:
        return self.vehicle.owner
