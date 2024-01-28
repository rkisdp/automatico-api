from django.urls import re_path

from . import views

app_name = "users"

urlpatterns = (
    re_path(
        r"^/?$",
        views.UserListView.as_view(),
        name="list",
    ),
    re_path(
        r"^/(?P<user_id>\d+)/?$",
        views.UserDetailView.as_view(),
        name="detail",
    ),
    re_path(
        r"^/(?P<user_id>\d+)/workshops/?$",
        views.UserWorkshopView().as_view(),
        name="workshops",
    ),
)
