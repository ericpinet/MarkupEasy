from rest_framework import serializers
from rest_framework import viewsets

from api.models import Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name', 'creation_date', 'user')


class ProjectViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for projects.
    """
    queryset = Project.objects.all().order_by('-id')
    serializer_class = ProjectSerializer
