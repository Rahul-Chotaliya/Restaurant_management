from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        print(request.user.is_authenticated,'ppopopopppppppopoppp',request.user)
        return request.user.is_authenticated and request.user.is_admin