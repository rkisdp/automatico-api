from rest_framework import routers

from . import views

app_name = "vehicles"

router = routers.DefaultRouter()
router.register(r"brands", views.VehicleBrandModelViewSet)
router.register(r"", views.VehicleModelViewSet)

urlpatterns = []

urlpatterns += router.urls
