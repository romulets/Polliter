# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Theme(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class UserThemes(models.Model):
    user = models.ForeignKey(User, related_name='themes')
    theme = models.ForeignKey(Theme, related_name='users')
