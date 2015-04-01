from django.db import models

# Create your models here.
class DataSet(models.Model):
    license_title = models.CharField(max_length=225)
    maintainer = models.CharField(max_length=225)
    private = models.BooleanField(default=False)
    maintainer_email = models.EmailField()
    num_tags = models.IntegerField()
    id_string = models.CharField(max_length=225)
    metadata_created = models.DateTimeField()
    license = models.CharField(max_length=225)
    metadata_modified = models.DateTimeField()
    author = models.CharField(max_length=225)
    author_email = models.EmailField()
    state = models.CharField(max_length=225)
    version = models.IntegerField()
    licence_id = models.CharField(max_length=225)
    type_string = models.CharField(max_length=225)
    num_resources = models.IntegerField()
    organization = models.CharField(max_length=225)
    name = models.CharField(max_length=225)
    is_open = models.BooleanField(default=False)
    notes_rendered = models.TextField()
    url = models.CharField(max_length=225)
    ckan_url = models.CharField(max_length=225)
    notes = models.TextField()
    owner_org = models.CharField(max_length=225)
    ratings_average = models.IntegerField()
    ratings_count = models.IntegerField()
    title = models.CharField(max_length=225)
    revision_id = models.CharField(max_length=225)
    #extras- make a function that will add them all to a hash


#needs join
class Resource(models.Model):
    resource_group_id = models.CharField(max_length=225)
    cache_last_updated = models.DateTimeField()
    package_id = models.CharField(max_length=225)
    webstore_last_updated = models.DateTimeField()
    id_string = models.CharField(max_length=225)
    size = models.CharField(max_length=225)
    last_modified = models.DateTimeField()
    hash_string = models.CharField(max_length=225)
    description = models.TextField()
    format_type = models.CharField(max_length=225)
    mimetype_inner = models.CharField(max_length=225)
    mimetype = models.CharField(max_length=225)
    cache_url = models.CharField(max_length=225)
    name = models.CharField(max_length=225)
    created = models.DateTimeField()
    url = models.CharField(max_length=225)
    webstore_url = models.CharField(max_length=225)
    position = models.IntegerField()
    resource_type = models.CharField(max_length=225)

#needs join
class Tag(models.Model):
    name = models.CharField(max_length=225)

class TrackingSummary(models.Model):
    data_set = models.ForeignKey(DataSet)
    total = models.IntegerField(default=0)
    recent = models.IntegerField(default=0)

#needs join
class Group(models.Model):
    id_string = models.CharField(max_length=225)
