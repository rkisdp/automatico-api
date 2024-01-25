from django.urls import path

from . import views

app_name = "users"

urlpatterns = (
    path(
        "",
        views.UserListView.as_view(),
        name="list",
    ),
    path(
        "/<int:user_id>",
        views.UserDetailView.as_view(),
        name="detail",
    ),
    path(
        "/<int:user_id>/workshops",
        views.UserWorkshopView().as_view(),
        name="workshops",
    ),
)
