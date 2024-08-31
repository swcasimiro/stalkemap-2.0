from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('<str:slug>/', views.location_list, name='location-list'),
    path('<slug:slug>/<slug:hood_slug>/', views.location_detail, name='hood'),
]
