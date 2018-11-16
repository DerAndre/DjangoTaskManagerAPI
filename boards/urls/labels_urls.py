"""
__author__ = "Andre Litty"
__copyright__ = "Copyright 2018"
__license__ = "GPL"
__email__ = "alittysw@gmail.com"
"""
from django.urls import include, path
from rest_framework import routers

from boards.views import LabelViewSet

# Router provides routes for standard CRUD functionality
router = routers.DefaultRouter()
router.register(r'', LabelViewSet, basename='label')

urlpatterns = [
    path('labels/', include(router.urls)),
]
