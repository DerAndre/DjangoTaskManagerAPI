"""
__author__ = "Andre Litty"
__copyright__ = "Copyright 2018"
__license__ = "GPL"
__email__ = "alittysw@gmail.com"
"""
from django.urls import include, path
from rest_framework import routers

from boards.views import ListViewSet

# Router provides routes for standard CRUD functionality
router = routers.DefaultRouter()
router.register(r'', ListViewSet, basename='list')

urlpatterns = [
    path('lists/', include(router.urls)),
]
