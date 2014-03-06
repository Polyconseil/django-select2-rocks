from django.conf.urls import patterns, url, include
from django.contrib import admin

from tastypie import api as tastypie_api
from testproj.testapp.api import BeachResource

from rest_framework import routers
from testapp.views import BeachViewSet

admin.autodiscover()

# Tastypie
tastypie_api_v1 = tastypie_api.Api(api_name='v1')
tastypie_api_v1.register(BeachResource())


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'beaches', BeachViewSet)

urlpatterns = patterns('testproj.testapp.views',
    url(r'^$', 'index', name='index'),
    url(r'^json/$', 'json_beaches', name='json_beaches'),
    url(r'^tastypie/', include(tastypie_api_v1.urls)),
    url(r'^restframework/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
