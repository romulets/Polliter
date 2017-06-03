# -*- coding: utf-8 -*-
from rest_framework import serializers
from models import Politician


class PoliticianSerializer(serializers.ModelSerializer):

    class Meta:
        model = Politician
        fields = '__all__'
        depth = 2
