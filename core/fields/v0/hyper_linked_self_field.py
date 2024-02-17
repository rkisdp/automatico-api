from rest_framework.relations import HyperlinkedIdentityField


class HyperLinkSelfField(HyperlinkedIdentityField):
    lookup_field = None
    lookup_fields = None
    lookup_url_kwargs = None

    def __init__(self, view_name=None, **kwargs):
        self.lookup_fields = kwargs.pop("lookup_fields", self.lookup_fields)
        self.lookup_url_kwargs = kwargs.pop(
            "lookup_url_kwargs", self.lookup_url_kwargs
        )
        super().__init__(view_name, **kwargs)

    def get_url(self, obj, view_name, request, format):
        kwargs = {}
        if self.lookup_field is not None:
            lookup_value = getattr(obj, self.lookup_field)
            kwargs = {self.lookup_url_kwarg: lookup_value}

        if self.lookup_url_kwargs is not None:
            for field, kwarg in zip(self.lookup_fields, self.lookup_url_kwargs):
                kwargs[kwarg] = getattr(obj, field)
        return self.reverse(
            view_name, kwargs=kwargs, request=request, format=format
        )
