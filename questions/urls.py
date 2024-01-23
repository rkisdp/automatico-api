from django.urls import path

from . import views

app_name = "questions"

urlpatterns = (
    path(
        "",
        views.QuestionViewSet.as_view({"get": "list", "post": "create"}),
        name="list",
    ),
    path(
        "/<int:question_id>",
        views.QuestionViewSet.as_view(
            {"get": "retrieve", "patch": "partial_update"}
        ),
        name="detail",
    ),
    path(
        "/<int:question_id>/responses",
        views.QuestionResponseViewSet.as_view(
            {"get": "list", "post": "create"}
        ),
        name="response-list",
    ),
    path(
        "/<int:question_id>/responses/<int:response_id>",
        views.QuestionResponseViewSet.as_view(
            {"get": "retrieve", "patch": "partial_update"}
        ),
        name="response-detail",
    ),
)
