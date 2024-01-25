from django.urls import path

from . import views

app_name = "services"

urlpatterns = (
    path(
        "/<int:service_id>",
        views.ServiceViewSet.as_view({"get": "retrieve"}),
        name="detail",
    ),
    path(
        "/<int:service_id>/histories",
        views.ServiceHistoryViewSet.as_view({"get": "list", "post": "create"}),
        name="histories",
    ),
    path(
        "/statuses",
        views.ServiceStatusViewSet.as_view({"get": "list"}),
        name="status-list",
    ),
    path(
        "/statuses/<int:status_id>",
        views.ServiceStatusViewSet.as_view({"get": "retrieve"}),
        name="status-detail",
    ),
)
