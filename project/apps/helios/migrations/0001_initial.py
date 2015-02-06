# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HTTPRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(unique=True, max_length=512, verbose_name=b'URL')),
                ('duration', models.IntegerField()),
                ('method', models.CharField(max_length=32, choices=[(b'GET', b'GET'), (b'POST', b'POST'), (b'PUT', b'PUT'), (b'DELETE', b'DELETE')])),
            ],
            options={
                'verbose_name': 'HTTP Request',
            },
            bases=(models.Model,),
        ),
    ]
