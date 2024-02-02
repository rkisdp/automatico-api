from django.contrib.auth import get_user_model
from rest_framework import serializers

from security.email import send_verification_code


class PrivateUserSerializer(serializers.ModelSerializer):
    services_count = serializers.IntegerField(
        read_only=True,
        source="services.count",
        default=0,
    )
    vehicles_count = serializers.IntegerField(
        read_only=True,
        source="vehicles.count",
        default=0,
    )
    workshops_count = serializers.IntegerField(
        read_only=True,
        source="workshops.count",
        default=0,
    )
    image_url = serializers.ImageField(
        read_only=True,
        source="image",
        use_url=True,
    )
    url = serializers.HyperlinkedIdentityField(
        view_name="users:detail",
        lookup_field="id",
        lookup_url_kwarg="user_id",
    )

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "email_verified",
            "phone_number",
            "phone_number_verified",
            "services_count",
            "vehicles_count",
            "workshops_count",
            "image_url",
            "url",
            "date_joined",
            "last_login",
        )

        read_only_fields = (
            "id",
            "email_verified",
            "phone_number_verified",
            "date_joined",
            "last_login",
        )

    def update(self, instance, validated_data):
        email = validated_data.pop("email", None)
        if email and email.lower() != instance.email:
            instance.email = email
            instance.email_verified = False
            instance.save()

            send_verification_code(
                user=instance,
                code_type="EVC",
                email_template="email_verification_code",
                email_subject="Verificación de Correo Electrónico",
            )

        return super().update(instance, validated_data)
