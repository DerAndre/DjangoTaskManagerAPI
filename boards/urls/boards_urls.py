"""
__author__ = "Andre Litty"
__copyright__ = "Copyright 2018"
__license__ = "GPL"
__email__ = "alittysw@gmail.com"
"""
from django.urls import include, path
from rest_framework import routers

from boards.views import BoardViewSet

# Router provides routes for standard CRUD functionality
router = routers.DefaultRouter()
router.register(r'', BoardViewSet, basename='board')

urlpatterns = [
    path('boards/', include(router.urls)),
]
