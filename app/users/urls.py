from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('eventer_response/', views.eventer_response, name='eventer_response'),
    path('eventer_my_stats/', views.eventer_my_stats, name='eventer_my_stats'),
    path('eventer_stats/assist/', views.eventer_stats, name='eventer_stats'),
    path('eventer_response_faction', views.eventer_response_faction, name='eventer_response_faction'),
    path('eventer_response_faction/<int:pk>/update/', views.ResponseFactionUpdateView.as_view(),
         name='eventer_response_faction_update'),
    path('eventer_my_response/', views.eventer_my_response, name='eventer_my_response'),
    path('eventer_my_response/<int:pk>/update/', views.ResponseFactionArchiveUpdateView.as_view(),
         name='eventer_response_faction_archive_update'),
    path('eventer_response_faction_archive', views.eventer_response_faction_archive,
         name='eventer_response_faction_archive'),
    path('eventer_list/', views.eventer_list, name='eventer_list'),
    path('eventer_list/<int:pk>/update/', views.EventsArchiveUpdateView.as_view(),
         name='events_archive_update'),
    path('eventer_list/archive/', views.eventer_list_archive, name='eventer_list_archive'),
    # assist
    path('event_list/assist/', views.event_list, name='event_list_assist'),
    path('event_list/assist/<int:pk>/update/', views.EventsUpdateView.as_view(),
         name='events_assist_update'),
]
