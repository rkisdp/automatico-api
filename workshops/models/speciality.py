from django.db import models
from django.utils.translation import gettext_lazy as _
from django_softdelete.models import SoftDeleteModel
from rest_framework.exceptions import ValidationError


class Speciality(SoftDeleteModel):
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

    @staticmethod
    def validate_unique_name(name: str) -> None:
        if Speciality.objects.filter(name__iexact=name).exists():
            raise ValidationError(
                {"name": _("Speciality with this name already exists.")}
            )
