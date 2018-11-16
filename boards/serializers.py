"""
__author__ = "Andre Litty"
__copyright__ = "Copyright 2018"
__license__ = "GPL"
__email__ = "alittysw@gmail.com"
"""
from rest_framework import serializers

from .models import Board, Label, List


class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = '__all__'
        read_only_fields = ['created_by', 'modified_at', 'modified_by', 'archived']


class ListSerializer(serializers.ModelSerializer):

    class Meta:
        model = List
        fields = '__all__'
        read_only_fields = ['created_by', 'modified_at', 'modified_by', 'archived']


class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Label
        fields = '__all__'
        read_only_fields = ['created_by', 'modified_at', 'modified_by', 'archived']
