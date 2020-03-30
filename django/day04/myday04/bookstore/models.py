from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField("书名", max_length=50, default="", unique=True)
    pub = models.CharField("出版社", max_length=100, default="")
    price = models.DecimalField("定价", max_digits=5, decimal_places=2, default=0.0)
    market_price = models.DecimalField("零售价", max_digits=5, decimal_places=2, default=0.0)
    is_active = models.BooleanField("是否活跃", default=True)
    class Meta:
        # 该模型所用的数据表在数据库里的名称 (设置完成后需要立刻更新同步数据库)
        db_table = "book"
        verbose_name = "图书"
        verbose_name_plural = verbose_name

    # def __str__(self):
    #     return f"{self.title}-{self.pub}-{self.price}-{self.market_price}"

class Author(models.Model):
    name = models.CharField("姓名", max_length=20, default="")
    age = models.IntegerField("年龄", default=1)
    email = models.EmailField("邮箱", null=True)

    class Meta:
        db_table = "author"
        verbose_name = "作者"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.name}--{self.age}--{self.email}"