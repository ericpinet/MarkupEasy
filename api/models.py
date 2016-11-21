from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime
from django.db import models


def user_project_directory_path(instance, filename):
    """
    File will be uploaded to MEDIA_ROOT/<project.id>/<filename>
    :param instance:
    :param filename:
    :return:
    """
    return 'data/{0}/{1}'.format(instance.project.id, filename)


class Project(models.Model):
    """
    Project class

    Representation of project of users.
    """
    name = models.CharField(max_length=255)
    creation_date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class File(models.Model):
    """
    Representation of a file in project
    """
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=datetime.now, blank=True)
    file = models.FileField(upload_to=user_project_directory_path)

