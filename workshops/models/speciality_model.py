from django.db import models
from django.utils.translation import gettext_lazy as _


class SpecialityModel(models.Model):
    id = models.AutoField(
        verbose_name=_("id"),
        help_text=_("Speciality id"),
        primary_key=True,
        unique=True,
        editable=False,
    )
    name = models.CharField(
        verbose_name=_("speciality"),
        help_text=_("Workshop speciality"),
        max_length=50,
        unique=True,
    )

    class Meta:
        verbose_name = _("speciality")
        verbose_name_plural = _("specialities")
        db_table = "speciality"

    def __str__(self) -> str:
        return self.name
