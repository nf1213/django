# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wisertogether', '0007_auto_20150402_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='groups',
            field=models.ManyToManyField(to='wisertogether.Group', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dataset',
            name='resources',
            field=models.ManyToManyField(to='wisertogether.Resource', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dataset',
            name='tags',
            field=models.ManyToManyField(to='wisertogether.Tag', blank=True),
            preserve_default=True,
        ),
    ]
