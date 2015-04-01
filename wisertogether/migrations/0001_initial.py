# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('license_title', models.CharField(max_length=225)),
                ('maintainer', models.CharField(max_length=225)),
                ('private', models.BooleanField()),
                ('maintainer_email', models.EmailField(max_length=75)),
                ('num_tags', models.IntegerField()),
                ('id_string', models.CharField(max_length=225)),
                ('metadata_created', models.DateTimeField()),
                ('license', models.CharField(max_length=225)),
                ('metadata_modified', models.DateTimeField()),
                ('author', models.CharField(max_length=225)),
                ('author_email', models.EmailField(max_length=75)),
                ('state', models.CharField(max_length=225)),
                ('version', models.IntegerField()),
                ('licence_id', models.CharField(max_length=225)),
                ('type_string', models.CharField(max_length=225)),
                ('num_resources', models.IntegerField()),
                ('organization', models.CharField(max_length=225)),
                ('name', models.CharField(max_length=225)),
                ('is_open', models.BooleanField()),
                ('notes_rendered', models.TextField()),
                ('url', models.CharField(max_length=225)),
                ('ckan_url', models.CharField(max_length=225)),
                ('notes', models.TextField()),
                ('owner_org', models.CharField(max_length=225)),
                ('ratings_average', models.IntegerField()),
                ('ratings_count', models.IntegerField()),
                ('title', models.CharField(max_length=225)),
                ('revision_id', models.CharField(max_length=225)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_string', models.CharField(max_length=225)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resource_group_id', models.CharField(max_length=225)),
                ('cache_last_updated', models.DateTimeField()),
                ('package_id', models.CharField(max_length=225)),
                ('webstore_last_updated', models.DateTimeField()),
                ('id_string', models.CharField(max_length=225)),
                ('size', models.CharField(max_length=225)),
                ('last_modified', models.DateTimeField()),
                ('hash_string', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('format_type', models.CharField(max_length=225)),
                ('mimetype_inner', models.CharField(max_length=225)),
                ('mimetype', models.CharField(max_length=225)),
                ('cache_url', models.CharField(max_length=225)),
                ('name', models.CharField(max_length=225)),
                ('created', models.DateTimeField()),
                ('url', models.CharField(max_length=225)),
                ('webstore_url', models.CharField(max_length=225)),
                ('position', models.IntegerField()),
                ('resource_type', models.CharField(max_length=225)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=225)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrackingSummary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.IntegerField(default=0)),
                ('recent', models.IntegerField(default=0)),
                ('data_set', models.ForeignKey(to='wisertogether.DataSet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
