"""
__author__ = "Andre Litty"
__copyright__ = "Copyright 2018"
__license__ = "GPL"
__email__ = "alittysw@gmail.com"
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('members.urls')),
    path('api/', include('cards.urls')),
    path('api/', include('boards.urls.boards_urls')),
    path('api/', include('boards.urls.labels_urls')),
    path('api/', include('boards.urls.lists_urls'))
]
