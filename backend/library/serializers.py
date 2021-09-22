from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, HyperlinkedRelatedField
from .models import Author, Bio, Book


class AuthorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BioSerializer(ModelSerializer):
    author = HyperlinkedRelatedField(read_only=True, view_name='author-detail')

    class Meta:
        model = Bio
        fields = '__all__'


class BookSerializer(ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'

