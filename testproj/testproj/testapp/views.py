# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from rest_framework import viewsets, serializers, filters

from testproj.testapp.models import Beach, SelectedBeach
from testproj.testapp import forms


def index(request):
    if request.method == 'POST':
        form = forms.SelectedBeachForm(data=request.POST)
        if form.is_valid():
            selected_beach = form.save()
            messages.success(
                request,
                u"JSON Beach '%s' has been selected." % selected_beach.json_beach)
            return redirect('index')
    else:
        selected_beach = SelectedBeach.objects.get(pk=1)
        form = forms.SelectedBeachForm(instance=selected_beach)

    return render(request, 'index.html', {'form': form})


def json_beaches(request):
    q = request.GET.get('q')
    results = Beach.objects.order_by('name')
    if q:
        results = results.filter(name__icontains=q)

    # Rename the key 'name' in 'text'
    flat_results = list(results.values_list('id', 'name'))
    results = [{'id': item[0], 'text': item[1]} for item in flat_results]
    return HttpResponse(
        json.dumps(results, ensure_ascii=False),
        content_type='application/json; charset=utf-8')


# REST Framework
class BeachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beach
        fields = ('id', 'name')


class BeachViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BeachSerializer
    queryset = Beach.objects.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('^name',)
    ordering = 'name'
