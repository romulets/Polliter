# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import Theme, UserThemes


# Create your views here.
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_theme(request, **kwargs):
    user = request.user
    theme = Theme.objects.get(pk=kwargs['id'])
    userTheme, created = UserThemes.objects.get_or_create(user=user, theme=theme)
    return Response({'created': created}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_theme(request, **kwargs):
    user = request.user
    theme = Theme.objects.get(pk=kwargs['id'])
    try:
        userTheme = UserThemes.objects.get(user=user, theme=theme)
        removed = True
    except Exception as e:
        removed = False
        return Response({'removed': removed, 'msg': str(e)}, status=status.HTTP_200_OK)

    return Response({'removed': removed}, status=status.HTTP_200_OK)
