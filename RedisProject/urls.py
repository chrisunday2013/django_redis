from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from main.views import *

router = routers.DefaultRouter()

#API
router.register(r'musician', MusicianViewSet, basename='musician')
router.register(r'album', AlbumViewSet, basename='album')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls), name='api'),
]