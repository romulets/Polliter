# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from politician.models import Politician
from theme.models import Theme
from django.contrib.auth.models import User


# Create your models here.
class Topic (models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(max_length=500, null=True)
    date = models.DateTimeField(null=False, auto_now_add=True)
    reference = models.URLField(max_length=1000, null=True)
    image = models.URLField(max_length=1000, null=True)
    politicians = models.ManyToManyField(Politician)
    themes = models.ManyToManyField(Theme)

    def __str__(self):
        return self.title


class Vote (models.Model):
    positive = models.BooleanField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        if self.positive:
            return '%d aprova "%d"' % (self.user.first_name, self.topic.title)
        else:
            return '%d não aprova "%d"' % (self.user.first_name, self.topic.title)