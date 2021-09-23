from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from .models import Author, Bio, Book
from .serializers import AuthorSerializer, BioSerializer, BookSerializer


# class AuthorView(APIView):
#     def get(self, request, format=None):
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data)
#
#
# @api_view(['GET'])
# @renderer_classes(JSONRenderer)
# def author_view(request):
#     authors = Author.objects.all()
#     serializer = AuthorSerializer(authors, many=True)
#     return Response(serializer.data)
#
#
# class AuthorView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
#     serializer_class = AuthorSerializer
#     queryset = Author.objects.all()


# class AuthorView(ViewSet):
#
#     @action(detail=False, methods=['GET'])
#     def get_name(self, request, pk=None):
#         author = get_object_or_404(Author, pk=(pk or 1))
#         # serializer = AuthorSerializer(author)
#         return Response({'first_name': author.first_name})
#
#     def list(self, request):
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk):
#         author = get_object_or_404(Author, pk=pk)
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data)


# class AuthorListView(ListAPIView):
#     serializer_class = AuthorSerializer
#     queryset = Author.objects.all()
#
#
# class AuthorRetrieveView(RetrieveAPIView):
#     serializer_class = AuthorSerializer
#     queryset = Author.objects.all()


class AuthorLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 1


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    filterset_fields = ['first_name']
    pagination_class = AuthorLimitOffsetPagination


    # def get_queryset(self):
    #     if 'first_name' in self.request.query_params:
    #         return Author.objects.filter(first_name=self.request.query_params['first_name'])
    #     return Author.objects.all()


#
# class BioViewSet(ModelViewSet):
#     serializer_class = BioSerializer
#     queryset = Bio.objects.all()
#
#
# class BookViewSet(ModelViewSet):
#     serializer_class = BookSerializer
#     queryset = Book.objects.all()
