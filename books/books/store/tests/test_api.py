from django.urls import reverse
from rest_framework.test import APITestCase
from ..models import Book
from ..serializers import BookSerializer
from rest_framework import status


class BookApiTestCase(APITestCase):
    def test_get(self):
        book_1 = Book.objects.create(name='Test_book 1', price=25)
        book_2 = Book.objects.create(name='Test_book 2', price=55)
        url = reverse('book-list')
        print(url)
        response = self.client.get(url)
        serializer_data = BookSerializer([book_1, book_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
