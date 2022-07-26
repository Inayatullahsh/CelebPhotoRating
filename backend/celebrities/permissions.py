from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
)


class IsPhotoOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.celebrity.created_by == request.user


class IsOwnerOrReadOnly(BasePermission):

    message = "You must be the owner of the object."

    """
    Authenticated users can only see list view
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    """
    Custom Permission to check if the user is the owner of the object.
    """

    def has_object_permission(self, request, view, obj):
        """
        Read permissions are allowed to any request so we'll always
        allow GET, HEAD, or OPTIONS requests
        """
        if request.method in SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author of a post
        return obj.created_by == request.user
