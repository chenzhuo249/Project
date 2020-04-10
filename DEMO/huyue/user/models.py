from django.db import models

# Create your models here.
class Goods(models.Model):

    name = models.CharField("名称", max_length=30, default="")
    price = models.DecimalField("价格", max_digits=7, decimal_places=2, default=0.0)
    count = models.IntegerField("数量",default=0)
    