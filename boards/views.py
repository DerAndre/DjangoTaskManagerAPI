"""
__author__ = "Andre Litty"
__copyright__ = "Copyright 2018"
__license__ = "GPL"
__email__ = "alittysw@gmail.com"
"""

from rest_framework import viewsets

from .models import Board, Label, List
from .serializers.boards_serializers import BoardSerializer
from .serializers.labels_serializers import LabelSerializer
from .serializers.lists_serializers import ListSerializer


class BoardViewSet(viewsets.ModelViewSet):
    """
    ViewSet to provide CRUD functionality for Board model
    """
    serializer_class = BoardSerializer

    def get_queryset(self):
        """
        Can be adjusted to filter boards more precisely
        :return: QuerySet
        """
        return Board.objects.all()


class ListViewSet(viewsets.ModelViewSet):
    """
    ViewSet to provide CRUD functionality for List model
    """
    serializer_class = ListSerializer

    def get_queryset(self):
        """
        Can be adjusted to filter lists more precisely
        :return: QuerySet
        """
        return List.objects.all()


class LabelViewSet(viewsets.ModelViewSet):
    """
    ViewSet to provide CRUD functionality for Label model
    """
    serializer_class = LabelSerializer

    def get_queryset(self):
        """
        Can be adjusted to filter labels more precisely
        :return: QuerySet
        """
        return Label.objects.all()
