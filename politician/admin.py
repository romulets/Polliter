# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import PoliticalParty, Politician

# Register your models here.
admin.site.register(PoliticalParty)
admin.site.register(Politician)