from django.urls import path

from . import views

app_name = "documentation"

urlpatterns = (
    path(
        "/schema",
        views.SpectacularAPIView.as_view(),
        name="schema",
    ),
    path(
        "/swagger",
        views.SpectacularSwaggerView.as_view(url_name="documentation:schema"),
        name="swagger",
    ),
    path(
        "/redoc",
        views.SpectacularRedocView.as_view(url_name="documentation:schema"),
        name="redoc",
    ),
)
