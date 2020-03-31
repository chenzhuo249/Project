from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=20)


class Book(models.Model):
    title = models.CharField(verbose_name="书名", max_length=40)
    authors = models.ManyToManyField(Author)
