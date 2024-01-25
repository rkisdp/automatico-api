from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from core.fields.v0_8 import HyperLinkSelfField
from workshops.models import WorkshopContactModel


class WorkshopContactListSerializer(serializers.ModelSerializer):
    url = HyperLinkSelfField(
        view_name="workshops:contact-detail",
        lookup_field="id",
        help_text=_("URL to the workshop contact."),
    )

    class Meta:
        model = WorkshopContactModel
        fields = (
            "id",
            "name",
            "value",
            "url",
        )
        read_only_fields = ("id",)
