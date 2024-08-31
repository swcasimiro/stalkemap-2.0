from django.urls import path, include
from django.views.generic import TemplateView

from .api import ResponseEventApiViewSet, EventLocalApiViewSet, EventGlobalApiViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'event_global', EventGlobalApiViewSet, basename='global')
router.register(r'event_local', EventLocalApiViewSet, basename='local')
router.register(r'response_event', ResponseEventApiViewSet, basename='response-event')

urlpatterns = router.urls
