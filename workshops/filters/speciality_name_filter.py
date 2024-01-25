from django.db.models import Q
from django_filters import CharFilter
from django_filters.constants import EMPTY_VALUES


class SpecialityNameFilter(CharFilter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs
        query = Q()
        for speciality in value.split(","):
            query |= Q(specialities__name__iexact=speciality)
        return qs.filter(query)
