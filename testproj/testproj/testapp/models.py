from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Beach(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class SelectedBeach(models.Model):
    json_beach = models.ForeignKey(Beach, blank=True, null=True, related_name='json')
    tastypie_beach_contains = models.ForeignKey(Beach, blank=True, null=True, related_name='tp_contains')
    tastypie_beach_starts = models.ForeignKey(Beach, blank=True, null=True, related_name='tp_starts')
    rest_framework_beach = models.ForeignKey(Beach, blank=True, null=True, related_name='rest')
