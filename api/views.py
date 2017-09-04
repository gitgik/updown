from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import File
from .serializers import FileUploadSerializer
from django_filters.rest_framework import DjangoFilterBackend


class FileUploadViewSet(ModelViewSet):
    """A viewset to handle file uploads."""
    queryset = File.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ("name",)

    def perform_create(self, serializer):
        owner = self.request.user
        serializer.save(owner=owner, _file=self.request.data.get('_file'))
