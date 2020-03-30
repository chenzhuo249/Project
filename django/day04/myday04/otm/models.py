from django.db import models

# Create your models here.
class Pub(models.Model):
    #一
    name = models.CharField(max_length=20, verbose_name="社名")

class Book(models.Model):
    #多
    title = models.CharField(max_length=20, verbose_name="书名")
    pub = models.ForeignKey(Pub)