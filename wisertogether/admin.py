from django.contrib import admin
from wisertogether.models import DataSet, Tag, Group, Resource

# Register your models here.
admin.site.register(DataSet)
admin.site.register(Tag)
admin.site.register(Group)
admin.site.register(Resource)
