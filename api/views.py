from django.shortcuts import render
from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.viewsets import ModelViewSet
from .models import File
from .serializers import FileUploadSerializer


class FileUploadViewSet(ModelViewSet):
    """A viewset to handle file uploads."""
    queryset = File.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser)

    def perform_create(self, serializer):
        owner = self.request.user
        serializer.save(owner=owner, _file=self.request.data.get('_file'))
