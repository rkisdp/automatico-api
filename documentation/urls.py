from django.urls import re_path

from . import views

app_name = "documentation"

urlpatterns = (
    re_path(
        r"^/schema/?$",
        views.SpectacularAPIView.as_view(),
        name="schema",
    ),
    re_path(
        r"^/swagger/?$",
        views.SpectacularSwaggerView.as_view(url_name="documentation:schema"),
        name="swagger",
    ),
    re_path(
        r"^/redoc/?$",
        views.SpectacularRedocView.as_view(url_name="documentation:schema"),
        name="redoc",
    ),
)
