"""
__author__ = "Andre Litty"
__copyright__ = "Copyright 2018"
__license__ = "GPL"
__email__ = "alittysw@gmail.com"
"""

from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.test import APITestCase

from boards.models import Board, List
from task_management.settings import ALLOWED_HOSTS

from .models import Card
from .serializers import CardSerializer


class CardsTest(APITestCase):
    """
    Defines all test cases for the cards app
    """

    def setUp(self):
        """
        Setup for all following test cases, creating board, list and card instance in test database, defining urls to
        check
        :return: None
        """
        board = Board.objects.create(name='Test Board')
        test_list = List.objects.create(board=board)
        card = Card.objects.create(title='TestCard', list=test_list)

        self.list_url = '%s%s%s' % ('http://', ALLOWED_HOSTS[0], '/api/cards/')
        self.single_url = '%s%s%s%s' % ('http://', ALLOWED_HOSTS[0], '/api/cards/', str(card.id) + '/')
        self.wrong_url = '%s%s%s' % ('http://', ALLOWED_HOSTS[0], '/api/carts/')

    def test_get_all_cards(self):
        response = self.client.get(self.list_url)
        all_cards_from_db = Card.objects.all()

        serializer = CardSerializer(all_cards_from_db, many=True)
        serialized_json = JSONRenderer().render(serializer.data)

        self.assertEqual(response.content, serialized_json)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_card(self):
        response = self.client.get(self.single_url)
        card_from_db = Card.objects.first()

        serializer = CardSerializer(card_from_db)
        serialized_json = JSONRenderer().render(serializer.data)

        self.assertEqual(response.content, serialized_json)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_wrong_card_url(self):
        response = self.client.get(self.wrong_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_card(self):
        payload = {
            'title': 'Second Test Card',
            'list': List.objects.first().id
        }
        response = self.client.post(self.list_url, payload)
        card_from_db = Card.objects.last()

        serializer = CardSerializer(card_from_db)
        serialized_json = JSONRenderer().render(serializer.data)

        self.assertEqual(response.content, serialized_json)
        self.assertEqual(Card.objects.all().count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_card(self):
        response = self.client.delete(self.single_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Card.objects.first().archived, True)
