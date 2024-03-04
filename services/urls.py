from django.urls import path

from . import views

app_name = "services"

urlpatterns = (
    path(
        "/<int:service_id>",
        views.ServiceView.as_view(),
        name="detail",
    ),
    path(
        "/<int:service_id>/histories",
        views.ServiceHistoryView.as_view(),
        name="histories",
    ),
    path(
        "/statuses",
        views.ServiceStatusListView.as_view(),
        name="status-list",
    ),
)
