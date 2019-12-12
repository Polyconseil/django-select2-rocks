from django import forms

from select2rocks.widgets import AjaxSelect2Widget, Select2TextInput


def label_from_instance_with_pk(obj, val):
    """Associates a label with the pk of the object that generated it.

    This is needed because we cannot rely on the order elements will appear
    in select2. By doing a binding like this, we are sure to associate a pk
    with the correct label (labels are shown, pks are submitted)."""
    return u"{pk}:{val}".format(pk=obj.pk, val=val)


class Select2ChoiceField(forms.ChoiceField):
    widget = AjaxSelect2Widget

    def __init__(self, choices, widget, label_from_instance=None, *args, **kwargs):
        kwargs['choices'] = self.choices = choices
        kwargs['widget'] = widget
        super(Select2ChoiceField, self).__init__(*args, **kwargs)
        self._label_from_instance = label_from_instance or super(Select2ChoiceField, self).label_from_instance
        self.widget.field = self

    def label_from_instance(self, obj):
        return self._label_from_instance(obj)

    def to_python(self, value):
        ret = ''
        for obj in self.choices:
            if obj[0] == value:
                return obj
        return ret

    def clean(self, value):
        self.validate(value)
        self.run_validators(value)
        return value[0] if isinstance(value, tuple) else value

class Select2ModelChoiceField(forms.ModelChoiceField):
    widget = AjaxSelect2Widget

    def __init__(self, queryset, widget, label_from_instance=None, *args, **kwargs):
        kwargs['queryset'] = queryset
        kwargs['widget'] = widget
        super(Select2ModelChoiceField, self).__init__(*args, **kwargs)
        self._label_from_instance = label_from_instance or super(Select2ModelChoiceField, self).label_from_instance
        self.widget.field = self

    def label_from_instance(self, obj):
        label = self._label_from_instance(obj)
        return label_from_instance_with_pk(obj, label)


class Select2ModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    widget = AjaxSelect2Widget

    def __init__(self, queryset, widget, label_from_instance=None, *args, **kwargs):
        kwargs['queryset'] = queryset
        kwargs['widget'] = widget
        super(Select2ModelMultipleChoiceField, self).__init__(*args, **kwargs)
        if not self.widget.select2_options:
            self.widget.select2_options = {}
        self.widget.select2_options.update({'multiple': True})
        self._label_from_instance = label_from_instance or super(Select2ModelMultipleChoiceField, self).label_from_instance
        self.widget.field = self

    def label_from_instance(self, objects):
        return ','.join([label_from_instance_with_pk(obj, self._label_from_instance(obj)) for obj in objects])

    def to_python(self, values):
        return super(Select2ModelMultipleChoiceField, self).to_python(values.split(','))

    def clean(self, value):
        return super(Select2ModelMultipleChoiceField, self).clean(value.split(',') if value else None)
