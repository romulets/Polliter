# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-03 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('politician', '0003_userpoliticians'),
    ]

    operations = [
        migrations.AddField(
            model_name='politician',
            name='following',
            field=models.BooleanField(default=False),
        ),
    ]