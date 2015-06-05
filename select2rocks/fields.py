from django import forms

from select2rocks.widgets import AjaxSelect2Widget


class Select2FieldMixin(object):
    widget = AjaxSelect2Widget

    def label_from_instance(self, obj):
        if self._label_from_instance is not None:
            val = self._label_from_instance(obj)
        else:
            val = super(Select2FieldMixin, self).label_from_instance(obj)
        return "{key}:{val}".format(key=obj.pk, val=val)


class Select2ModelChoiceField(Select2FieldMixin, forms.ModelChoiceField):

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


class Select2ModelMultipleChoiceField(Select2FieldMixin, forms.ModelMultipleChoiceField):

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
        self._label_from_instance = label_from_instance
        self.widget.field = self

    def label_from_instance(self, objects):
        return ','.join([super(Select2ModelMultipleChoiceField, self).label_from_instance(obj) for obj in objects])

    def to_python(self, values):
        return super(Select2ModelMultipleChoiceField, self).to_python(values.split(','))
