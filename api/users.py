from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework import viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the user ViewSet
    """

    class Meta:
        """
        Meta for the user ViewSet
        """
        model = User
        fields = ('url', 'id', 'first_name', 'last_name', 'email')


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for users.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
