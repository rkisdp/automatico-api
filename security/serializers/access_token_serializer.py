from typing import Any

from rest_framework.serializers import CharField
from rest_framework_simplejwt import serializers


class AccessTokenSerializer(serializers.TokenObtainPairSerializer):
    access = CharField(read_only=True)

    def validate(self, attrs: dict[str, Any]) -> dict[str, str]:
        data = super().validate(attrs)
        del data["refresh"]
        return data
