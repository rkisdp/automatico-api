from django_filters import rest_framework as django_filters

from workshops.filters import SpecialityNameFilter, VehicleBrandNameFilter
from workshops.models import WorkshopModel


class WorkshopFilterSet(django_filters.FilterSet):
    specialities = SpecialityNameFilter()
    brands = VehicleBrandNameFilter()

    class Meta:
        model = WorkshopModel
        fields = ("specialities", "brands")
