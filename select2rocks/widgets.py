import json

import django
from django import forms
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.template import loader
from django.utils.encoding import force_text

from select2rocks.settings import SELECT2_OPTIONS, SELECT2_ATTRS


class Select2TextInput(forms.TextInput):
    is_required = False

    def get_context(self, name, value, attrs=None):
        context = {
            'type': self.input_type,
            'name': name,
            'hidden': self.is_hidden,
            'required': self.is_required,
        }

        if value is not None:
            # Only add the value if it is non-empty
            context['value'] = self.format_value(value)

        if django.VERSION >= (1, 11):
            context['attrs'] = self.build_attrs(self.attrs, attrs)
        else:
            context['attrs'] = self.build_attrs(attrs)

        for key, attr in context['attrs'].items():
            if attr == 1:
                # 1 == True so 'key="1"' will show up only as 'key'
                if not isinstance(attr, bool):
                    context['attrs'][key] = str(attr)

        return context

    def render(self, name, value, attrs=None, **kwargs):
        context = self.get_context(name, value, attrs=attrs or {})

        if django.VERSION >= (1, 10):
            return loader.render_to_string(
                self.template_name, context=context)

        return loader.render_to_string(
            self.template_name,
            dictionary=context,
            context_instance=None)


class AjaxSelect2Widget(Select2TextInput):
    template_name = 'select2rocks/ajax_select2.html'

    def __init__(self, url=None, url_name=None, url_kwargs=None, select2_options=None, *args, **kwargs):
        self.url = None
        self.url_name = None
        self.url_kwargs = None

        # The URL can be given or reversed in get_context()
        if url is not None:
            self.url = url
        else:
            self.url_name = url_name
            if url_kwargs is not None:
                self.url_kwargs = url_kwargs

        self.select2_options = select2_options if select2_options is not None else {}

        super(AjaxSelect2Widget, self).__init__(*args, **kwargs)

    def get_context(self, name, value, attrs=None):
        if not self.url:
            # Try to reverse it
            self.url = reverse(self.url_name, kwargs=self.url_kwargs)

        attrs.update(SELECT2_ATTRS)

        options = {}
        options.update(SELECT2_OPTIONS)
        options.update(self.select2_options)
        options.update({'url': self.url})

        ctx = super(AjaxSelect2Widget, self).get_context(name, value, attrs)
        if 'placeholder' in options:
            # Resolve lazy ugettext
            options['placeholder'] = force_text(options['placeholder'])

        ctx['select2_options'] = json.dumps(options)
        try:
            # Django's to_python returns instances sorted by their pks (ASC) in
            # case of a multiple selection, we cannot rely on the order of pks
            # in `value` anymore
            instance = self.field.to_python(value) if value else None
        except ValidationError:
            instance = None
        ctx['text'] = self.field.label_from_instance(instance) if instance else ''
        return ctx
