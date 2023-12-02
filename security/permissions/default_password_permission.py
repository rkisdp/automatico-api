from rest_framework.permissions import BasePermission


class DefaultPasswordPermission(BasePermission):
    message = (
        "You must change your default password before you "
        "can perform this action."
    )

    def has_permission(self, request, view):
        return not request.user.default_password
