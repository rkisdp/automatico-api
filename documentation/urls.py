from django.urls import path
from drf_spectacular import views
from rest_framework.versioning import QueryParameterVersioning

app_name = "documentation"

urlpatterns = (
    path(
        "schema/",
        views.SpectacularAPIView.as_view(
            versioning_class=QueryParameterVersioning
        ),
        name="schema",
    ),
    path(
        "swagger/",
        views.SpectacularSwaggerView.as_view(
            url_name="documentation:schema",
            versioning_class=QueryParameterVersioning,
        ),
        name="swagger",
    ),
    path(
        "redoc/",
        views.SpectacularRedocView.as_view(
            url_name="documentation:schema",
            versioning_class=QueryParameterVersioning,
        ),
        name="redoc",
    ),
)
