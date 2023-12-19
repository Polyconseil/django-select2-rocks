from django.urls import re_path
from django.contrib import admin

from testproj.testapp.views import BeachList, index, json_beaches

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^json/$', json_beaches, name='json_beaches'),
    re_path(r'^restframework/$', BeachList.as_view(), name='rest_beach_list'),
    re_path(r'^admin/', admin.site.urls),
]
