from django.db import models

class User(models.Model):

    nickname = models.CharField("昵称", max_length=11)
    age = models.IntegerField("年龄", default=0)


