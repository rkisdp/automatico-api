from django.urls import re_path

from . import views

app_name = "services"

urlpatterns = (
    re_path(
        r"^/(?P<service_id>\d+)/?$",
        views.ServiceView.as_view(),
        name="detail",
    ),
    re_path(
        r"^/(?P<service_id>\d+)/histories/?$",
        views.ServiceHistoryView.as_view(),
        name="histories",
    ),
    re_path(
        r"^/statuses/?$",
        views.ServiceStatusListView.as_view(),
        name="status-list",
    ),
)
