# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-17 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0003_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='image',
            field=models.URLField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='reference',
            field=models.URLField(max_length=1000, null=True),
        ),
    ]
