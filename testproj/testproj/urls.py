from django.conf.urls import url, include
from django.contrib import admin

from tastypie import api as tastypie_api
from testproj.testapp.api import BeachResource

from testproj.testapp.views import BeachList, index, json_beaches

admin.autodiscover()

# Tastypie
tastypie_api_v1 = tastypie_api.Api(api_name='v1')
tastypie_api_v1.register(BeachResource())

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^json/$', json_beaches, name='json_beaches'),
    url(r'^tastypie/', include(tastypie_api_v1.urls)),
    url(r'^restframework/$', BeachList.as_view(), name='rest_beach_list'),
    url(r'^admin/', include(admin.site.urls)),
]
