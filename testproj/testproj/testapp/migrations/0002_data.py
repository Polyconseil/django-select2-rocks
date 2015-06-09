# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def add_beaches(apps, schema_editor):
    names = (
        u"Les Jaunais",
        u"Pointe de Chemoulin",
        u"Plage de la Petite Vallée",
        u"Plage de Géorama",
        u"Plage de Grand Traict",
        u"Plage de M. Hulot",
        u"La Courance",
        u"Plage de l'Ève",
        u"Virechat",
        u"Trébézy",
        u"Porcé",
        u"Bonne Anse",
        u"Plage du Rocher du Lion",
        u"Belle Fontaine",
        u"Plage de Kerloupiots",
        u"Plage de Kerlédé",
        u"Ker Villès",
        u"Plage de Villès Martin",
        u"Plage de Saint-Nazaire",
    )
    Beach = apps.get_model("testapp", "Beach")
    for name in names:
        Beach.objects.create(name=name)

    SelectedBeach = apps.get_model("testapp", "SelectedBeach")
    SelectedBeach.objects.create(
        json_beach=Beach.objects.get(name=u"Plage de M. Hulot"),
        tastypie_beach_contains=Beach.objects.get(name=u"Les Jaunais"),
        rest_framework_beach=Beach.objects.get(name=u"Plage de la Petite Vallée"),
        tastypie_beach_starts=Beach.objects.get(name=u"Pointe de Chemoulin")
    )


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_beaches)
    ]
