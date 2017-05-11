# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Theme(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
