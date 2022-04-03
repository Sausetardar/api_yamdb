from rest_framework import permissions, exceptions


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (request.user.is_authenticated
                and request.user.role in ['admin', 'sadmin'])


class ReviewCommentPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
                request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE' and request.user.role == 'moderator':
            return True
        return (
                request.method in permissions.SAFE_METHODS
                or obj.author == request.user
        )
