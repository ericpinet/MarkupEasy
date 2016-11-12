from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Project(models.Model):
    """
    Project class

    Representation of project of users.
    """
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date created')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
