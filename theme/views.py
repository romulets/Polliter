# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from models import Theme, UserThemes
from serializers import ThemeSerializer
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'theme/templates/home.html')


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def list_themes(request):
    themes = Theme.objects.all()
    map(lambda t: t.populate_following(request.user), themes)
    serializer = ThemeSerializer(themes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_theme(request, **kwargs):
    user = request.user
    theme = Theme.objects.get(pk=kwargs['id'])
    UserThemes.objects.get_or_create(user=user, theme=theme)
    theme.populate_following(user)
    return Response({'following': theme.following}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_theme(request, **kwargs):
    user = request.user
    theme = Theme.objects.get(pk=kwargs['id'])
    try:
        user_theme = UserThemes.objects.get(user=user, theme=theme)
        user_theme.delete()
    except Exception:
        pass

    theme.populate_following(user)
    return Response({'following': theme.following}, status=status.HTTP_200_OK)
