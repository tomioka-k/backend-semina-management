from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminUserOrAuthenticatedReadOnly(BasePermission):
   
    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True
        elif request.method in SAFE_METHODS and request.user and request.user.is_authenticated:
            return True
        else:
            return False