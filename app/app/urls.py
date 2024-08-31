from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from locations.views import index
from .yasg import urlpatterns as doc_urls

urlpatterns = [
                  path('admin/', admin.site.urls),

                  # rest framework
                  path('api/', include('api.urls')),
                  path('api/drf-auth/', include('rest_framework.urls')),  # classic auth DRF

                  # djoser
                  path('api/auth/', include('djoser.urls')),
                  re_path(r'^auth/', include('djoser.urls.authtoken')),

                  # simple-jwt
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

                  # just url
                  path('', index, name='index'),
                  path('location-list/', include('locations.urls')),
                  path('events-list/', include('events.urls')),
                  path("user/", include('users.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Подключение static FILES

urlpatterns += doc_urls  # подключение swagger

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
