from django.conf.urls import url
from django.contrib import admin

from testproj.testapp.views import BeachList, index, json_beaches

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^json/$', json_beaches, name='json_beaches'),
    url(r'^restframework/$', BeachList.as_view(), name='rest_beach_list'),
    url(r'^admin/', admin.site.urls),
]
