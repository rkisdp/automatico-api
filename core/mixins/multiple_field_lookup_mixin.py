from rest_framework.generics import get_object_or_404


class MultipleFieldLookupMixin:
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """

    def get_object(self):
        queryset = self.filter_queryset(super().get_queryset())
        kwargs = {}

        for field, kwarg in zip(self.lookup_fields, self.lookup_url_kwargs):
            kwargs[field] = self.kwargs[kwarg]
        obj = get_object_or_404(queryset, **kwargs)
        self.check_object_permissions(self.request, obj)
        return obj
