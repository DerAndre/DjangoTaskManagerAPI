"""
__author__ = "Andre Litty"
__copyright__ = "Copyright 2018"
__license__ = "GPL"
__email__ = "alittysw@gmail.com"
"""

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Member


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class MemberSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Member
        fields = '__all__'
        read_only_fields = ['modified_at', 'archived']

    def create(self, validated_data):
        """
        Override create method to create a django auth user for every new member
        :param validated_data: Dict
        :return: Member
        """
        user_data = validated_data.pop('user', None)
        if user_data:
            user_name = '%s%s' % (user_data.get('first_name'), user_data.get('last_name'))
            user = User(username=user_name, **user_data)
            user.save()
        return Member.objects.create(user=user)

    def update(self, instance, validated_data):
        """
        Override update method to rename django auth user for corresponding member
        :param instance: Member
        :param validated_data: Dict
        :return: Member
        """
        user_data = validated_data.pop('user', None)
        if user_data:
            if user_data.get('first_name'):
                instance.user.first_name = user_data.get('first_name') if user_data.get('first_name') else \
                    instance.user.first_name
                instance.user.last_name = user_data.get('last_name') if user_data.get('last_name') else \
                    instance.user.last_name
            instance.user.save()
        return instance
