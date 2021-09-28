from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from .views import SeminarViewSet

router = routers.DefaultRouter()
router.register('', SeminarViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
