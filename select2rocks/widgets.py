import json

from django import forms
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
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
        if self.is_hidden:
            context['hidden'] = True

        if value is None:
            value = ''

        if value != '':
            # Only add the value if it is non-empty
            context['value'] = self._format_value(value)

        context['attrs'] = self.build_attrs(attrs)

        for key, attr in context['attrs'].items():
            if attr == 1:
                # 1 == True so 'key="1"' will show up only as 'key'
                if not isinstance(attr, bool):
                    context['attrs'][key] = str(attr)

        return context

    def render(self, name, value, attrs=None, **kwargs):
        context = self.get_context(name, value, attrs=attrs or {}, **kwargs)
        return loader.render_to_string(
            self.template_name,
            dictionary=context,
            context_instance=None)


class AjaxSelect2Widget(Select2TextInput):
    template_name = 'select2rocks/ajax_select2.html'

    def __init__(self, *args, **kwargs):
        self.url = None
        self.url_name = None
        self.url_kwargs = None

        # The URL can be given or reversed in get_context()
        try:
            self.url = kwargs.pop('url')
        except KeyError:
            self.url_name = kwargs.pop('url_name')
            if 'url_kwargs' in kwargs:
                self.url_kwargs = kwargs.pop('url_kwargs')

        if 'select2_options' in kwargs:
            self.select2_options = kwargs.pop('select2_options')
        else:
            self.select2_options = {}

        super(AjaxSelect2Widget, self).__init__(*args, **kwargs)

    def get_context(self, name, value, attrs=None):
        if not self.url:
            # Try to reverse it
            if self.url_kwargs:
                self.url = reverse(self.url_name, kwargs=self.url_kwargs)
            else:
                self.url = reverse(self.url_name)

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
            instance = self.field.to_python(value) if value else None
        except ValidationError:
            instance = None
        ctx['text'] = self.field.label_from_instance(instance) if instance else ''
        return ctx
