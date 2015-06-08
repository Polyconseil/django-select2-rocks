from django import forms

from select2rocks.widgets import AjaxSelect2Widget


def label_from_instance_with_pk(obj, val):
    """Add pk to label to associate label to input in multiple fields"""
    return "{pk}:{val}".format(pk=obj.pk, val=val)


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
        self._label_from_instance = label_from_instance or super(Select2ModelChoiceField, self).label_from_instance
        self.widget.field = self

    def label_from_instance(self, obj):
        label = self._label_from_instance(obj)
        return label_from_instance_with_pk(obj, label)


class Select2ModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    widget = AjaxSelect2Widget

    def __init__(self, queryset, empty_label="---------", cache_choices=False,
                 required=True, widget=None, label=None, initial=None,
                 help_text='', to_field_name=None, label_from_instance=None,
                 *args, **kwargs):
        super(Select2ModelMultipleChoiceField, self).__init__(
            queryset, cache_choices, required, widget,
            label, initial, help_text, *args, **kwargs)
        if not self.widget.select2_options:
            self.widget.select2_options = {}
        self.widget.select2_options.update({'multiple': True})
        self._label_from_instance = label_from_instance or super(Select2ModelMultipleChoiceField, self).label_from_instance
        self.widget.field = self

    def label_from_instance(self, objects):
        return ','.join([label_from_instance_with_pk(obj, self._label_from_instance(obj)) for obj in objects])

    def to_python(self, values):
        return super(Select2ModelMultipleChoiceField, self).to_python(values.split(','))
