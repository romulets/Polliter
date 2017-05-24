# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-24 22:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('politician', '0002_auto_20170511_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPoliticians',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('politician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='politician.Politician')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='politicians', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
