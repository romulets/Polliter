# -*- coding: utf-8 -*-
from rest_framework import serializers
from models import Topic, Vote


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'
        depth = 2
