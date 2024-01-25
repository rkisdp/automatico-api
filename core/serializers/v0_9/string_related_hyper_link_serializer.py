from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.relations import Hyperlink
from rest_framework.reverse import reverse


class StringRelatedHyperLinkSerializer(serializers.Serializer):
    lookup_field = "id"
    lookup_url_kwarg = None
    lookup_fields = None
    lookup_url_kwargs = None

    def __init__(self, view_name, **kwargs):
        self.view_name = view_name
        self.lookup_field = kwargs.pop("lookup_field", self.lookup_field)
        self.lookup_url_kwarg = kwargs.pop(
            "lookup_url_kwarg", self.lookup_field
        )
        self.lookup_fields = kwargs.pop("lookup_fields", self.lookup_fields)
        self.lookup_url_kwargs = kwargs.pop(
            "lookup_url_kwargs", self.lookup_url_kwargs
        )
        super().__init__(**kwargs)

    name = serializers.CharField(
        help_text=_("The name of the resource."),
        read_only=True,
    )
    url = serializers.URLField(
        help_text=_("The URL of the resource."),
        read_only=True,
    )

    def get_url(self, obj, view_name, request, format):
        kwargs = {}
        if self.lookup_field is not None:
            lookup_value = getattr(obj, self.lookup_field)
            kwargs = {self.lookup_url_kwarg: lookup_value}

        if self.lookup_url_kwargs is not None:
            for kwarg in self.lookup_url_kwargs:
                field = self.lookup_fields[self.lookup_url_kwargs.index(kwarg)]
                lookup_value = getattr(obj, field)
                kwargs[kwarg] = lookup_value
        return reverse(view_name, kwargs=kwargs, request=request, format=format)

    def to_representation(self, value):
        request = self.context.get("request")
        format = self.context.get("format", None)
        url = self.get_url(
            obj=value,
            view_name=self.view_name,
            request=request,
            format=format,
        )

        if url is None:
            return None

        return {
            "name": str(value),
            "url": Hyperlink(url, value),
        }
