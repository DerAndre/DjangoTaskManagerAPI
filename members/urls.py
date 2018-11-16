"""
__author__ = "Andre Litty"
__copyright__ = "Copyright 2018"
__license__ = "GPL"
__email__ = "alittysw@gmail.com"
"""
from django.urls import include, path
from rest_framework import routers

from .views import MemberViewSet

# Router provides routes for standard CRUD functionality
router = routers.DefaultRouter()
router.register(r'', MemberViewSet, basename='member')

urlpatterns = [
    path('members/', include(router.urls))
]
