# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wisertogether', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='is_open',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dataset',
            name='private',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
