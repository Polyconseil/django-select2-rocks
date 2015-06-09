# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='SelectedBeach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('json_beach', models.ForeignKey(related_name='json', blank=True, to='testapp.Beach', null=True)),
                ('rest_framework_beach', models.ForeignKey(related_name='rest', blank=True, to='testapp.Beach', null=True)),
                ('tastypie_beach_contains', models.ForeignKey(related_name='tp_contains', blank=True, to='testapp.Beach', null=True)),
                ('tastypie_beach_starts', models.ForeignKey(related_name='tp_starts', blank=True, to='testapp.Beach', null=True)),
            ],
        ),
    ]
