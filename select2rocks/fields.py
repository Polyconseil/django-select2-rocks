from django import forms

from select2rocks.widgets import AjaxSelect2Widget


class Select2ModelChoiceField(forms.ModelChoiceField):
    widget = AjaxSelect2Widget

    def __init__(self, queryset, empty_label="---------", cache_choices=False,
                 required=True, widget=None, label=None, initial=None,
                 help_text='', to_field_name=None, *args, **kwargs):
        super(Select2ModelChoiceField, self).__init__(
            queryset, empty_label, cache_choices,
            required, widget, label, initial,
            help_text, to_field_name, *args, **kwargs)
        self.widget.field = self
