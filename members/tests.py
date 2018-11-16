"""
__author__ = "Andre Litty"
__copyright__ = "Copyright 2018"
__license__ = "GPL"
__email__ = "alittysw@gmail.com"
"""

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.test import APITestCase

from task_management.settings import ALLOWED_HOSTS

from .models import Member
from .serializers import MemberSerializer


class MembersTest(APITestCase):
    """
    Defines all test cases for the members app
    """

    def setUp(self):
        """
        Setup for all following test cases, creating user and member instance in test database, defining urls to check
        :return: None
        """
        user = User.objects.create(first_name='Test', last_name='User', username='TestUser')
        member = Member.objects.create(user=user)

        self.list_url = '%s%s%s' % ('http://', ALLOWED_HOSTS[0], '/api/members/')
        self.single_url = '%s%s%s%s' % ('http://', ALLOWED_HOSTS[0], '/api/members/', str(member.id) + '/')
        self.wrong_url = '%s%s%s' % ('http://', ALLOWED_HOSTS[0], '/api/membars/')

    def test_get_all_members(self):
        response = self.client.get(self.list_url)
        all_members_from_db = Member.objects.all()

        serializer = MemberSerializer(all_members_from_db, many=True)
        serialized_json = JSONRenderer().render(serializer.data)

        self.assertEqual(response.content, serialized_json)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_member(self):
        response = self.client.get(self.single_url)
        member_from_db = Member.objects.first()

        serializer = MemberSerializer(member_from_db)
        serialized_json = JSONRenderer().render(serializer.data)

        self.assertEqual(response.content, serialized_json)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_wrong_member_url(self):
        response = self.client.get(self.wrong_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_member(self):
        payload = {
            'user': {
                'first_name': 'Second',
                'last_name': 'User'
            }
        }
        response = self.client.post(self.list_url, payload)
        member_from_db = Member.objects.last()

        serializer = MemberSerializer(member_from_db)
        serialized_json = JSONRenderer().render(serializer.data)

        self.assertEqual(response.content, serialized_json)
        self.assertEqual(Member.objects.all().count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_member(self):
        response = self.client.delete(self.single_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Member.objects.first().archived, True)
