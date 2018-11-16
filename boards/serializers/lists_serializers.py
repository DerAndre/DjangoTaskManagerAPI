"""
__author__ = "Andre Litty"
__copyright__ = "Copyright 2018"
__license__ = "GPL"
__email__ = "alittysw@gmail.com"
"""
from rest_framework import serializers

from cards.serializers import CardSerializer

from ..models import List


class ListSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, read_only=True)

    class Meta:
        model = List
        fields = '__all__'
        read_only_fields = ['created_by', 'modified_at', 'modified_by', 'archived']
