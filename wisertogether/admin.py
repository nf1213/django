from django.contrib import admin
from wisertogether.models import DataSet, Tag, Group, Resource

# Register your models here.
class GroupsInline(admin.TabularInline):
    model = Group.data_sets.through

class ResourcesInline(admin.TabularInline):
    model = Resource.data_sets.through

class TagsInline(admin.TabularInline):
    model = Tag.data_sets.through

class DataSetAdmin(admin.ModelAdmin):
    inlines = [GroupsInline, ResourcesInline, TagsInline]

admin.site.register(DataSet, DataSetAdmin)
admin.site.register(Tag)
admin.site.register(Group)
admin.site.register(Resource)
