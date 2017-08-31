"""
This class represents a serializer for the file model.
"""
from .models import File
from rest_framework import serializers


class FileUploadSerializer(serializers.ModelSerializer):
    """Define the file api representation."""

    class Meta:
        """Meta class"""

        model = File
        fields = ('_file', 'created')

