from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('event_response/', views.event_response, name='event_response'),
    path('event_success/', views.event_success, name='event_success'),
    path("global/", views.event_global, name='event-global'),
    path('local/', views.event_local, name='event-local'),
]
