from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)

    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_authenticated
        return True


class FollowPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
