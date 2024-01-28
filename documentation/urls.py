from django.urls import re_path
from drf_spectacular import views
from rest_framework.versioning import QueryParameterVersioning

app_name = "documentation"

urlpatterns = (
    re_path(
        r"^/schema/?$",
        views.SpectacularAPIView.as_view(
            versioning_class=QueryParameterVersioning
        ),
        name="schema",
    ),
    re_path(
        r"^/swagger/?$",
        views.SpectacularSwaggerView.as_view(
            url_name="documentation:schema",
            versioning_class=QueryParameterVersioning,
        ),
        name="swagger",
    ),
    re_path(
        r"^/redoc/?$",
        views.SpectacularRedocView.as_view(
            url_name="documentation:schema",
            versioning_class=QueryParameterVersioning,
        ),
        name="redoc",
    ),
)
