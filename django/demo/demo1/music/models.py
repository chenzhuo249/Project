from django.db import models

# Create your models here.
class Music(models.Model):

    title = models.CharField("音乐名",max_length=50,default='')
    #00000.00
    price = models.DecimalField("价格", max_digits=7,decimal_places=2, default=0.0)
    desc = models.CharField("简介", max_length=100, default='')

class Book(models.Model):
    title = models.CharField("书名", max_length=50, default="", unique=True)
    pub = models.CharField("出版社", max_length=100, default="")
    price = models.DecimalField("定价", max_digits=5, decimal_places=2, default=0.0)
    market_price = models.DecimalField("零售价", max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.title}-{self.pub}-{self.price}-{self.market_price}"

class Author(models.Model):
    name = models.CharField("姓名", max_length=20, default="")
    age = models.IntegerField("年龄", default=1)
    email = models.EmailField("邮箱", null=True)

