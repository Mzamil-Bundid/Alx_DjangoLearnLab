from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, OPTIONS requests (read-only) for all users
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow write operations only if the user is the author
        return obj.author == request.user