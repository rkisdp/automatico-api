from django.urls import path

from . import views

app_name = "reviews"

urlpatterns = (
    path(
        "",
        views.ReviewViewSet.as_view({"get": "list", "post": "create"}),
        name="list",
    ),
    path(
        "/<int:review_id>",
        views.ReviewViewSet.as_view(
            {"get": "retrieve", "patch": "partial_update"}
        ),
        name="detail",
    ),
    path(
        "/<int:review_id>/responses",
        views.ReviewResponseViewSet.as_view({"get": "list", "post": "create"}),
        name="response-list",
    ),
    path(
        "/<int:review_id>/responses/<int:response_id>",
        views.ReviewResponseViewSet.as_view(
            {"get": "retrieve", "patch": "partial_update"}
        ),
        name="response-detail",
    ),
)
