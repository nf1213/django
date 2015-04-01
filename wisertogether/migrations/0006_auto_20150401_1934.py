# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wisertogether', '0005_auto_20150401_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='resources',
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='tags',
        ),
        migrations.AddField(
            model_name='group',
            name='data_sets',
            field=models.ManyToManyField(to='wisertogether.DataSet'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resource',
            name='data_sets',
            field=models.ManyToManyField(to='wisertogether.DataSet'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tag',
            name='data_sets',
            field=models.ManyToManyField(to='wisertogether.DataSet'),
            preserve_default=True,
        ),
    ]
