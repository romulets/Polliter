# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from models import Politician, UserPoliticians
from serializers import PoliticianSerializer
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'politician/templates/home.html')


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def list_politicians(request):
    politicians = Politician.objects.all()
    map(lambda p: p.populate_following(request.user), politicians)
    serializer = PoliticianSerializer(politicians, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_politician(request, **kwargs):
    user = request.user
    politician = Politician.objects.get(pk=kwargs['id'])
    UserPoliticians.objects.get_or_create(user=user, politician=politician)
    politician.populate_following(user)
    return Response({'following': politician.following}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_politician(request, **kwargs):
    user = request.user
    politician = Politician.objects.get(pk=kwargs['id'])
    try:
        user_politician = UserPoliticians.objects.get(user=user, politician=politician)
        user_politician.delete()
    except Exception:
        pass

    politician.populate_following(user)
    return Response({'following': politician.following}, status=status.HTTP_200_OK)