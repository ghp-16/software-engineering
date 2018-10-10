from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=20)


class Publisher(models.Model):
    pub_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)


class Book(models.Model):
    book_name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    publish = models.ForeignKey(Publisher, on_delete=models.CASCADE)