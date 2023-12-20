from rest_framework import routers

from . import views

app_name = "services"

router = routers.DefaultRouter()
router.register("statuses", views.ServiceStatusViewSet)
router.register("histories", views.ServiceHistoryViewSet)
router.register("", views.ServiceViewSet)

urlpatterns = []

urlpatterns += router.urls
