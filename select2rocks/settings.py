from django.conf import settings

SELECT2_OPTIONS = {}

if hasattr(settings, 'SELECT2_OPTIONS'):
    SELECT2_OPTIONS.update(settings.SELECT2_OPTIONS)


SELECT2_ATTRS = {
    'style': 'width: 300px;',
}

if hasattr(settings, 'SELECT2_ATTRS'):
    SELECT2_ATTRS.update(settings.SELECT2_ATTRS)
