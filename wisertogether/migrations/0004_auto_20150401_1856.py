# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wisertogether', '0003_auto_20150401_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='tracking_summary',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='tracking_summary',
        ),
        migrations.DeleteModel(
            name='TrackingSummary',
        ),
        migrations.AddField(
            model_name='dataset',
            name='tracking_recent',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dataset',
            name='tracking_total',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resource',
            name='tracking_recent',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resource',
            name='tracking_total',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
