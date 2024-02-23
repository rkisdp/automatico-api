from django.db import models
from django.utils.translation import gettext_lazy as _
from django_softdelete.models import SoftDeleteModel


class VerificationCodeType(SoftDeleteModel):
    id = models.AutoField(
        verbose_name=_("id"),
        help_text=_("Autogenerated (non editable) verification code type id"),
        primary_key=True,
        unique=True,
        editable=False,
    )
    code = models.CharField(
        verbose_name=_("code"),
        help_text=_("Verification code type code"),
        max_length=5,
        unique=True,
    )
    name = models.CharField(
        verbose_name=_("name"),
        help_text=_("Verification code type name"),
        max_length=128,
        unique=True,
    )
    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("Verification code type description"),
        max_length=512,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("verification code type")
        verbose_name_plural = _("verification code types")
        db_table = "verification_code_type"

    def __str__(self):
        return self.name