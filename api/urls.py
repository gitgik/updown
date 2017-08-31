from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import FileUploadViewSet


file_list = FileUploadViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    url(r'files/', file_list, name="api.upload"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
