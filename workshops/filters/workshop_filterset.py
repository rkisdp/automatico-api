from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django_filters import rest_framework as django_filters

from workshops.filters import SpecialityNameFilter, VehicleBrandNameFilter
from workshops.models import WorkshopModel


class WorkshopFilterSet(django_filters.FilterSet):
    specialities = SpecialityNameFilter()
    brands = VehicleBrandNameFilter()
    distance = django_filters.NumberFilter(
        method="filter_distance",
        label="Max distance (km)",
    )

    class Meta:
        model = WorkshopModel
        fields = ("specialities", "brands")

    def filter_distance(self, queryset, name, value):
        try:
            lat, lon = self.request.META.get("HTTP_X_USER_LOCATION").split(",")
        except (AttributeError, ValueError):
            lat, lon = None, None

        if lat is None or lon is None:
            return queryset

        user_location = Point(float(lon), float(lat), srid=4326)
        queryset = queryset.annotate(
            distance=Distance("location", user_location)
        ).filter(distance__isnull=False, distance__lte=value * 1000)
        return queryset
