from rest_framework import permissions


class IsAdministrator(permissions.BasePermission):
    """Роль administrator"""
    def has_permission(self, request, view):
        return request.user.role == 'administrator'


class IsBusiness(permissions.BasePermission):
    """Роль business"""
    def has_permission(self, request, view):
        return request.user.role == 'business'


class IsManager(permissions.BasePermission):
    """Роль manager"""
    def has_permission(self, request, view):
        return request.user.role == 'manager'
