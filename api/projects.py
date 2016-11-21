from rest_framework import serializers
from rest_framework import viewsets

from api.models import Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    """
    Project Serializer
    """
    class Meta:
        model = Project
        fields = ('url', 'id', 'name', 'creation_date', 'user')

    def create(self, validated_data):
        project = Project.objects.create(**validated_data)
        return project


class ProjectViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for projects.
    """
    queryset = Project.objects.all().order_by('-id')
    serializer_class = ProjectSerializer
