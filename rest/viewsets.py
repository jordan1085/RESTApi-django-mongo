from rest_framework import viewsets

from .serializers import Bookserializer

from book.models import Book


class Bookserializer(viewsets.ModelViewSet):
    queruset = Book.objects.all()
    serializer_class = Bookserializer