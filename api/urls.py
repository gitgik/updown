from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import FileUploadViewSet


file_list = FileUploadViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

file_detail = FileUploadViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = format_suffix_patterns([
    url(r'files/$', file_list, name="file-list"),
    url(r'^files/(?P<pk>[0-9]+)/$',  file_detail, name="file-detail"),
])
