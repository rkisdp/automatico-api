from rest_framework.serializers import HyperlinkedRelatedField


class StringRelatedHyperLinkField(HyperlinkedRelatedField):
    def to_representation(self, value):
        return {
            "resource": str(value),
            "link": super().to_representation(value),
        }
