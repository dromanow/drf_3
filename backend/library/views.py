from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, BasePermission
from .models import Author, Bio, Book
from .serializers import AuthorSerializer, BioSerializer, BookSerializer


# class CustomPermission(BasePermission):
#
#     def has_permission(self, request, view):
#         return request.user.is_stuff


class AuthorViewSet(ModelViewSet):
    # permission_classes = [DjangoModelPermissions]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BioViewSet(ModelViewSet):
    serializer_class = BioSerializer
    queryset = Bio.objects.all()


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
