"""
This class represents a serializer for the file model.
"""
from .models import File
from rest_framework import serializers


class FileUploadSerializer(serializers.ModelSerializer):
    """Define the file api representation."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map this serializer to the a model and its fields"""

        model = File
        fields = ('id', 'file_id', '_file', 'owner', 'created')
        read_only_fields = ('file_id', 'created')

