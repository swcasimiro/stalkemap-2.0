from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Создание кастомного класса для проверки пользователя
    на административные права. """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)
