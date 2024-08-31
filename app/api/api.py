from requests import Response
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle

from .permissions import IsAdminOrReadOnly
from rest_framework.authentication import TokenAuthentication

from .serializers import (EventGlobalSerializer, EventLocalSerializer,
                          ResponseEventSerializer)
from events.models import Events, ResponseEvent

"""EVENTS APP API"""


class EventLocalApiViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.filter(type_status='Одобрено').filter(type_event='Локальные мероприятия')
    serializer_class = EventLocalSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'head', 'options', 'trace', 'patch', 'post', 'put']


class EventGlobalApiViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.filter(type_status='Одобрено').filter(type_event='Глобальные мероприятия')
    serializer_class = EventGlobalSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    http_method_names = ['get', 'head', 'options', 'trace', 'patch', 'post', 'put']


class ResponseEventApiViewSet(viewsets.ModelViewSet):
    queryset = ResponseEvent.objects.all()
    serializer_class = ResponseEventSerializer
    permission_classes = (IsAuthenticated,)
    throttle_classes = [AnonRateThrottle]


"""LOCATION APP API"""
