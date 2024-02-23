from rest_framework.permissions import BasePermission

from vehicles.models import Vehicle


class IsOwnerPermission(BasePermission):
    message = "You must be the owner of this vehicle to perform this action."

    def has_object_permission(self, request, view, obj: Vehicle):
        if not isinstance(obj, Vehicle):
            raise ValueError("obj must be an instance of Vehicle")
        return obj.owner == request.user
