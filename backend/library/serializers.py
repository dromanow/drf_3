from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, HyperlinkedRelatedField
from .models import Author, Bio, Book


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorSerializerV2(ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class BioSerializer(ModelSerializer):
    author = HyperlinkedRelatedField(read_only=True, view_name='author-detail')

    class Meta:
        model = Bio
        fields = '__all__'


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
