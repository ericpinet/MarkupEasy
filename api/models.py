from __future__ import unicode_literals

import os
import time

from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime
from django.core.files.storage import FileSystemStorage
from django.db import models


def user_project_directory_path(instance):
    """
    File will be uploaded to MEDIA_ROOT/<project.id>
    :param instance:
    :return:
    """
    return 'data/{0}/'.format(instance.id)


class Project(models.Model):
    """
    Project class

    Representation of project of users.
    """
    name = models.CharField(max_length=255)
    creation_date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_file_system_storage(self):
        """
        Return the FileSystemStorage for the project
        :return: Storage
        """
        return FileSystemStorage(user_project_directory_path(self), None, 777, 777)

    def get_files(self):
        """
        Return all files in project directory
        :return: Files
        """
        files = []

        try:
            storage = self.get_file_system_storage()

            files_name = storage.listdir(storage.location)
            for file in files_name[1]:
                if file:
                    files.append(ProjectFile(file, storage.location))

        except:
            files = []

        return files

    def get_files_count(self):
        """
        Return the count of files in project
        :return:
        """
        return len(self.get_files())


class ProjectFile:
    """
    Project File
    """
    def __init__(self, name, path):
        self.name = name
        self.path = path

        stat = os.stat(self.path + '/' + self.name)

        self.size = stat.st_size
        self.created = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(stat.st_birthtime))
        self.modified = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(stat.st_mtime))
        self.is_directory = stat.__class__

    def get_content(self):
        """
        Return file content
        :return: File content
        """
        with open(self.path + '/' + self.name, 'r') as content_file:
            content = content_file.read()

        return content

