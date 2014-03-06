from tastypie.resources import ModelResource
from tastypie.constants import ALL

from .models import Beach


class BeachResource(ModelResource):
    class Meta:
        queryset = Beach.objects.order_by('name')
        resource_name = 'beach'
        filtering = {
            'name': ALL
        }
