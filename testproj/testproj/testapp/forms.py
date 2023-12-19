from __future__ import unicode_literals

from django import forms
from django.utils.translation import gettext_lazy as _

import select2rocks

from testproj.testapp.models import Beach, SelectedBeach


class SelectedBeachForm(forms.ModelForm):

    class Meta:
        exclude = []
        model = SelectedBeach
        fields = [
            'json_beach',
            'rest_framework_beach',
            'rest_framework_beach_multi',
            'required_boolean',
        ]

    # Default JS backend
    json_beach = select2rocks.Select2ModelChoiceField(
        queryset=Beach.objects.all(),
        widget=select2rocks.AjaxSelect2Widget(
            url_name='json_beaches',
            select2_options={
                'placeholder': _("Select a beach"),
                'ajax': {
                    'quietMillis': 50
                }
            }))

    # REST Framework backend
    rest_framework_beach = select2rocks.Select2ModelChoiceField(
        queryset=Beach.objects.all(),
        required=False,
        widget=select2rocks.AjaxSelect2Widget(
            url_name='rest_beach_list',
            select2_options={'placeholder': _("Select a beach"),
                             'backend': 'restframework'}))

    # Multi select REST framework
    rest_framework_beach_multi = select2rocks.Select2ModelMultipleChoiceField(
        queryset=Beach.objects.all(),
        required=False,
        widget=select2rocks.AjaxSelect2Widget(
            url_name='rest_beach_list',
            select2_options={'placeholder': _("Select beaches"),
                             'backend': 'restframework'}))

    required_boolean = forms.BooleanField(
        required=True,
        help_text="Leave blank to raise a form error and test form restoration")
