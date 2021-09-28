from rest_framework.viewsets import ModelViewSet
from .models import Author, Bio, Book
from .serializers import AuthorSerializer, BioSerializer, BookSerializer


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BioViewSet(ModelViewSet):
    serializer_class = BioSerializer
    queryset = Bio.objects.all()


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
