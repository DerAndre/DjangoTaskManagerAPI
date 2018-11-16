"""
__author__ = "Andre Litty"
__copyright__ = "Copyright 2018"
__license__ = "GPL"
__email__ = "alittysw@gmail.com"
"""

from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.test import APITestCase

from task_management.settings import ALLOWED_HOSTS

from .models import Board, Label, List
from .serializers import BoardSerializer, LabelSerializer, ListSerializer


class BoardsTest(APITestCase):
    """
    Defines all test cases for the boards app
    """
    def setUp(self):
        """
        Setup for all following test cases, creating board instance in test database, defining urls to check
        :return: None
        """
        board = Board.objects.create(name='Test Board')

        self.list_url = '%s%s%s' % ('http://', ALLOWED_HOSTS[0], '/api/boards/')
        self.single_url = '%s%s%s%s' % ('http://', ALLOWED_HOSTS[0], '/api/boards/', str(board.id) + '/')
        self.wrong_url = '%s%s%s' % ('http://', ALLOWED_HOSTS[0], '/api/boarts/')

    def test_get_all_boards(self):
        response = self.client.get(self.list_url)
        all_boards_from_db = Board.objects.all()

        serializer = BoardSerializer(all_boards_from_db, many=True)
        serialized_json = JSONRenderer().render(serializer.data)

        self.assertEqual(response.content, serialized_json)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_board(self):
        response = self.client.get(self.single_url)
        board_from_db = Board.objects.first()

        serializer = BoardSerializer(board_from_db)
        serialized_json = JSONRenderer().render(serializer.data)

        self.assertEqual(response.content, serialized_json)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_wrong_board_url(self):
        response = self.client.get(self.wrong_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_board(self):
        payload = {
            'name': 'Test Board',
        }
        response = self.client.post(self.list_url, payload)
        board_from_db = Board.objects.last()

        serializer = BoardSerializer(board_from_db)
        serialized_json = JSONRenderer().render(serializer.data)

        self.assertEqual(response.content, serialized_json)
        self.assertEqual(Board.objects.all().count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_board(self):
        response = self.client.delete(self.single_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Board.objects.first().archived, True)


class LabelsTest(APITestCase):
    """
    Defines all test cases for the labels app
    """

    def setUp(self):
        """
        Setup for all following test cases, creating board, and label instance in test database, defining urls to check
        :return: None
        """
        board = Board.objects.create(name='Test Board')
        label = Label.objects.create(text='Test Label', board=board)

        self.list_url = '%s%s%s' % ('http://', ALLOWED_HOSTS[0], '/api/labels/')
        self.single_url = '%s%s%s%s' % ('http://', ALLOWED_HOSTS[0], '/api/labels/', str(label.id) + '/')
        self.wrong_url = '%s%s%s' % ('http://', ALLOWED_HOSTS[0], '/api/labells/')

    def test_get_all_labels(self):
        response = self.client.get(self.list_url)
        all_labels_from_db = Label.objects.all()

        serializer = LabelSerializer(all_labels_from_db, many=True)
        serialized_json = JSONRenderer().render(serializer.data)

        self.assertEqual(response.content, serialized_json)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_label(self):
        response = self.client.get(self.single_url)
        label_from_db = Label.objects.first()

        serializer = LabelSerializer(label_from_db)
        serialized_json = JSONRenderer().render(serializer.data)

        self.assertEqual(response.content, serialized_json)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_wrong_label_url(self):
        response = self.client.get(self.wrong_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_label(self):
        payload = {
            'text': 'Second Test Label',
            'board': Board.objects.first().id
        }
        response = self.client.post(self.list_url, payload)
        label_from_db = Label.objects.last()

        serializer = LabelSerializer(label_from_db)
        serialized_json = JSONRenderer().render(serializer.data)

        self.assertEqual(response.content, serialized_json)
        self.assertEqual(Label.objects.all().count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_label(self):
        response = self.client.delete(self.single_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Label.objects.first().archived, True)


class ListsTest(APITestCase):
    """
    Defines all test cases for the lists app
    """

    def setUp(self):
        """
        Setup for all following test cases, creating board and list instance in test database, defining urls to check
        :return: None
        """
        board = Board.objects.create(name='Test Board')
        test_list = List.objects.create(board=board)

        self.list_url = '%s%s%s' % ('http://', ALLOWED_HOSTS[0], '/api/lists/')
        self.single_url = '%s%s%s%s' % ('http://', ALLOWED_HOSTS[0], '/api/lists/', str(test_list.id) + '/')
        self.wrong_url = '%s%s%s' % ('http://', ALLOWED_HOSTS[0], '/api/lissts/')

    def test_get_all_lists(self):
        response = self.client.get(self.list_url)
        all_lists_from_db = List.objects.all()

        serializer = ListSerializer(all_lists_from_db, many=True)
        serialized_json = JSONRenderer().render(serializer.data)

        self.assertEqual(response.content, serialized_json)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_list(self):
        response = self.client.get(self.single_url)
        list_from_db = List.objects.first()

        serializer = ListSerializer(list_from_db)
        serialized_json = JSONRenderer().render(serializer.data)

        self.assertEqual(response.content, serialized_json)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_wrong_list_url(self):
        response = self.client.get(self.wrong_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_list(self):
        payload = {
            'board': Board.objects.first().id
        }
        response = self.client.post(self.list_url, payload)
        list_from_db = List.objects.last()

        serializer = ListSerializer(list_from_db)
        serialized_json = JSONRenderer().render(serializer.data)

        self.assertEqual(response.content, serialized_json)
        self.assertEqual(List.objects.all().count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_list(self):
        response = self.client.delete(self.single_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(List.objects.first().archived, True)
