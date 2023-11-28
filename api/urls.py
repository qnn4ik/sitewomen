from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import WomenAPIView


router = DefaultRouter()
router.register(r'women', WomenAPIView, basename='women')


urlpatterns = [
    path('api/v1/', include(router.urls)),
]
