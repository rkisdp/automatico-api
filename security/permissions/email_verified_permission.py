from rest_framework.permissions import BasePermission


class EmailVerifiedPermission(BasePermission):
    message = "You must verify your email before you can perform this action."

    def has_permission(self, request, view):
        return request.user.email_verified
