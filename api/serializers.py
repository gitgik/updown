"""
This class represents a serializer for the file model.
"""
from .models import File
from rest_framework import serializers


class FileUploadeSerializer(serializers.HyperlinkedModelSerializer):
    """Define the file api representation."""

    class Meta:
        """Meta class"""

        model = File
        fields = ('_file', 'created')

