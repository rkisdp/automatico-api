from django.db.models import Q
from django_filters import CharFilter
from django_filters.constants import EMPTY_VALUES


class VehicleBrandNameFilter(CharFilter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs
        query = Q()
        for brand in value.split(","):
            query |= Q(brands__name__iexact=brand)
        return qs.filter(query).distinct()
