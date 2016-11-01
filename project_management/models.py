from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date created')
