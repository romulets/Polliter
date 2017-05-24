# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from models import Politician, UserPoliticians


# Create your views here.
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_politician(request, **kwargs):
    user = request.user
    politician = Politician.objects.get(pk=kwargs['id'])
    userPolitician, created = UserPoliticians.objects.get_or_create(user=user, politician=politician)
    return Response({'created': created}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_politician(request, **kwargs):
    user = request.user
    politician = Politician.objects.get(pk=kwargs['id'])
    try:
        userPolitician = UserPoliticians.objects.get(user=user, politician=politician)
        userPolitician.delete()
        removed = True
    except Exception:
        removed = False
    return Response({'removed': removed}, status=status.HTTP_200_OK)