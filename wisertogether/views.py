from django.http import Http404
from wisertogether.serializers import DataSetSerializer
from wisertogether.models import DataSet

from rest_framework import generics

class DataSetList(generics.ListCreateAPIView):
    queryset = DataSet.objects.all()
    serializer_class = DataSetSerializer


class DataSetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataSet.objects.all()
    serializer_class = DataSetSerializer
