from rest_framework.permissions import BasePermission

from vehicles.models import VehicleModel


class IsOwnerPermission(BasePermission):
    message = "You must be the owner of this vehicle to perform this action."

    def has_object_permission(self, request, view, obj: VehicleModel):
        if not isinstance(obj, VehicleModel):
            raise ValueError("obj must be an instance of VehicleModel")
        return obj.owner == request.user
