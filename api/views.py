from django.shortcuts import render
from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet
from .models import File
from .serializers import FileUploadSerializer


class FileUploadViewSet(ModelViewSet):
    """A viewset to handle file uploads."""
    queryset = File.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = (FormParser, MultiPartParser)

    def perform_create(self, serializer):
        serializer.save(_file=self.request.data.get('_file'))
