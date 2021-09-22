from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.birthday_year}'


class Bio(models.Model):
    text = models.CharField(max_length=64)
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='bio')

    def __str__(self):
        return self.text


class Book(models.Model):
    title = models.CharField(max_length=64)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

