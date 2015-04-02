from wisertogether.models import DataSet, Group, Tag, Resource
from rest_framework import serializers

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource

class DataSetSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    groups = serializers.StringRelatedField(many=True)
    resources = ResourceSerializer(many=True, read_only=True)

    class Meta:
        model = DataSet
