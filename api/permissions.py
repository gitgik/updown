from rest_framework.permissions import BasePermission
from .models import File


class IsTheFileOwner(BasePermission):
    """This class represents a custom permission to allow only file owners to
    edit them.
    """

    def has_object_permission(self, request, view, obj):
        """Return True if the permission is granted to the owner."""
        if isinstance(obj, File):
            return obj.owner == request.user
        return obj.owner == request.user
