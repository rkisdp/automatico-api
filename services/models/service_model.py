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
        null=True,
        blank=True,
    )
    request_description = models.TextField(
        verbose_name=_("request description"),
        help_text=_("Request description"),
        max_length=255,
    )
    response_description = models.TextField(
        verbose_name=_("response description"),
        help_text=_("Response description"),
        max_length=255,
    )
    start_date = models.DateTimeField(
        verbose_name=_("start date"),
        help_text=_("Start date"),
        auto_now_add=True,
    )
    end_date = models.DateTimeField(
        verbose_name=_("end date"),
        help_text=_("End date"),
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("service")
        verbose_name_plural = _("services")
        db_table = "service"

    def __str__(self) -> str:
        return f"{self.vehicle} - {self.workshop}"
