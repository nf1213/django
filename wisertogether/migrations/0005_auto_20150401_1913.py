# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wisertogether', '0004_auto_20150401_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='groups',
            field=models.ManyToManyField(to='wisertogether.Group'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dataset',
            name='resources',
            field=models.ManyToManyField(to='wisertogether.Resource'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dataset',
            name='tags',
            field=models.ManyToManyField(to='wisertogether.Tag'),
            preserve_default=True,
        ),
    ]
