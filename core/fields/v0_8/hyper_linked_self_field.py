from rest_framework.relations import HyperlinkedIdentityField


class HyperLinkSelfField(HyperlinkedIdentityField):
    lookup_field = None

    def get_url(self, obj, view_name, request, format):
        kwargs = None
        if self.lookup_field is not None:
            lookup_value = getattr(obj, self.lookup_field)
            kwargs = {self.lookup_url_kwarg: lookup_value}
        return self.reverse(
            view_name, kwargs=kwargs, request=request, format=format
        )
