Django-select2-rocks
====================

Light integration glue between `Django <https://www.djangoproject.com/>`_ and
`Select2 <http://ivaynberg.github.com/select2/>`_.

This project is inspired by `Django-Select2 <http://django-select2.readthedocs.org/>`_ and
`django-select2light <https://github.com/ouhouhsami/django-select2light/>`_.

Django-select2-rocks is distributed under the BSD 2-clause license.


Installation
------------

1. pip install django_select2_rocks

2. add ``select2rocks`` to your ``INSTALL_APPS``

3. ``python manage.py collectstatic`` will install Django Select2 Rocks JS.

4. Include jQuery (1.7+), Select2 JS/CSS (not provided, tested with v3.4.5) and
   select2rocks/select2rocks.js in your templates.

5. Now, you can use ``Select2ModelChoiceField`` fields in your forms.


Design
------

Django-select2-rocks provides widgets to render and initialize Select2 inputs.

The widget rendering is based on Django with a further step which adds a JS
initialization for each input (on DOM ready). When a character is typed in the
input field, an AJAX request is sent to the URL associated to the field.

The widget API is designed to allow you to pass any arguments you want to
Select2 JS code (eg. allowClear option).

You can use various JSON views to answer to Select2 AJAX queries, and so to
adjust search terms or the format of the results, it's possible to extend the
default django-select2-rocks backend (see select2rocks-backends.js in testproj
for an example).


Example
-------

The testproj project contains examples with a simple JSON view, a Tastypie and a
Django REST framework view.

.. code-block:: python

   import select2rocks

   class BeachForm(forms.Form):
       beach = select2rocks.Select2ModelChoiceField(
           queryset=Beach.objects.all(),
           widget=select2rocks.AjaxSelect2Widget(url_name='json_beaches'))


Get the Code
------------

Django-select2-rocks is developed on GitHub:

    https://github.com/polyconseil/django-select2-rocks

You can either clone the public repository:

.. code-block:: bash

   $ git clone git://github.com/polyconseil/django-select2-rocks.git

Once you have a copy of the source, you can install it with:

.. code-block:: bash

   $ python setup.py install
