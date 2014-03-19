from django.test import TestCase

from testproj.testapp.models import Beach
from testproj.testapp import forms


class Select2RocksTestCase(TestCase):

    def test_rendering(self):
        form = forms.SelectedBeachForm()
        self.assertIn('id_json_beach', form.as_p())

        # Valid beach
        beach = Beach.objects.create(name='beach1')
        form = forms.SelectedBeachForm(data={'json_beach': beach.pk})
        self.assertIn('beach', form.as_p())

        # Invaling beach
        form = forms.SelectedBeachForm(data={'json_beach': 42})
        self.assertIn('That choice is not one of the available choices', form.as_p())
