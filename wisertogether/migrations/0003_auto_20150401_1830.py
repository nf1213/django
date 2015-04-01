# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wisertogether', '0002_auto_20150401_0105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trackingsummary',
            name='data_set',
        ),
        migrations.AddField(
            model_name='dataset',
            name='tracking_summary',
            field=models.ForeignKey(to='wisertogether.TrackingSummary', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resource',
            name='tracking_summary',
            field=models.ForeignKey(to='wisertogether.TrackingSummary', null=True),
            preserve_default=True,
        ),
    ]
