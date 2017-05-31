# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from django.core.paginator import Paginator
from django.db.models import Q
from topic.models import Topic, Vote
from topic.serializers import TopicSerializer


# Create your views here.
@api_view(['GET'])
def list_topics(request):
    try:
        page = int(request.GET.get('page', 1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1

    topics = Topic.objects.all().order_by('-date')
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def list_topics_for_user(request):
    user = request.user
    topics = Topic.objects.filter(
        Q(politicians__users__user=user) |
        Q(themes__users__user=user)
    ).order_by('-date').distinct()
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def vote(user, topic_id, positive):
    try:
        topic = Topic.objects.get(pk=topic_id)

        try:
            vote = Vote.objects.get(topic=topic, user=user)
        except Vote.DoesNotExist:
            vote = Vote(topic=topic, user=user)

        vote.positive = positive
        vote.save()
        return Response({}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def approve_topic(request, **kwargs):
    return vote(request.user, kwargs['id'], True)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def disapprove_topic(request, **kwargs):
    return vote(request.user, kwargs['id'], False)


@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def remove_vote_on_topic(request, **kwargs):
    try:
        topic = Topic.objects.get(pk=kwargs['id'])
        vote = Vote.objects.get(topic=topic, user=request.user)
        vote.delete()
        return Response({}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
