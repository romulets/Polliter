# -*- coding: utf-8 -*-
from rest_framework import serializers
from models import Theme


class ThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Theme
        fields = '__all__'
        depth = 2
