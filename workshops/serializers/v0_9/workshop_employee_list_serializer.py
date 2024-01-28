from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.fields.v0_9 import HyperLinkSelfField


def email_exists(email):
    if get_user_model().objects.filter(email__iexact=email).exists():
        return False
    raise ValidationError({"email": _(f"The email {email} does not exist.")})


class WorkshopEmployeeListSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[email_exists],
        help_text=_("User email."),
    )
    photo = serializers.ImageField(
        read_only=True,
        use_url=True,
        help_text=_("URL to the user's photo."),
    )
    url = HyperLinkSelfField(
        view_name="users:detail",
        lookup_field="id",
        lookup_url_kwarg="user_id",
        help_text=_("URL to the user."),
    )

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "photo",
            "phone_number",
            "url",
        )
        read_only_fields = (
            "first_name",
            "last_name",
            "photo",
            "phone_number",
        )
