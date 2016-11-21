from rest_framework import serializers
from rest_framework import viewsets

from api.models import File


class FileSerializer(serializers.HyperlinkedModelSerializer):
    """
    File Serializer
    """
    class Meta:
        model = File
        fields = ('url', 'id', 'name', 'creation_date', 'file', 'project')

    def create(self, validated_data):
        a_file = File.objects.create(**validated_data)
        return a_file


class FileViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for file.
    """
    queryset = File.objects.all().order_by('-id')
    serializer_class = FileSerializer
