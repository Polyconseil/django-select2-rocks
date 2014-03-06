from django import forms

from select2rocks.widgets import AjaxSelect2Widget


class Select2ModelChoiceField(forms.ModelChoiceField):
    widget = AjaxSelect2Widget

    def __init__(self, queryset, empty_label="---------", cache_choices=False,
                 required=True, widget=None, label=None, initial=None,
                 help_text='', to_field_name=None, label_from_instance=None,
                 *args, **kwargs):
        super(Select2ModelChoiceField, self).__init__(
            queryset, empty_label, cache_choices,
            required, widget, label, initial,
            help_text, to_field_name, *args, **kwargs)
        self._label_from_instance = label_from_instance
        self.widget.field = self

    def label_from_instance(self, obj):
        if self._label_from_instance is not None:
            return self._label_from_instance(obj)
        else:
            return super(Select2ModelChoiceField, self).label_from_instance(obj)
