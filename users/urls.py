from django.urls import path

from . import views

app_name = "users"

urlpatterns = (
    path("", views.UserViewSet.as_view({"get": "list"}), name="list"),
    path(
        "/<int:user_id>",
        views.UserViewSet.as_view({"get": "retrieve"}),
        name="detail",
    ),
)
