# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions


# Create your views here.
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_theme(request):
    pass


@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_theme(request):
    pass
