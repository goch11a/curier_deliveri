from rest_framework import permissions
from .models import CustomeUser

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == CustomeUser.admin


class DeleteUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in [CustomeUser.admin]
    

class AddUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in [CustomeUser.admin, CustomeUser.customer]

class ReadUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in [CustomeUser.admin, CustomeUser.curier, CustomeUser.customer]
    

class DeleteParcelPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in [CustomeUser.admin, CustomeUser.curier] 
    
class AddParcelPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in [CustomeUser.admin, CustomeUser.customer]


class ReadParcelPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in [CustomeUser.admin, CustomeUser.curier, CustomeUser.customer]
        