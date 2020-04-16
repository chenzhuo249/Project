from django.db import models

# Create your models here.
class Order(models.Model):
    order_number = models.CharField(verbose_name="订单编号", max_length=32, db_index=True, unique=True, default="")
    name = models.CharField(verbose_name="商品名称", max_length=50, default="")
    price = models.DecimalField(verbose_name="商品单价", max_digits=7, decimal_places=2, default=0.0)
    count = models.IntegerField(verbose_name="购买数量", default=0)
    img_path = models.ImageField(verbose_name="图片路径", default="")
    total = models.DecimalField(verbose_name="商品总价", max_digits=8, decimal_places=2, default=0.0)
    status = models.CharField(verbose_name="订单状态", max_length=1, default="2")
    create_time = models.DateField(verbose_name="订单创建时间", auto_now_add=True)
    update_time = models.DateField(verbose_name="订单修改时间", auto_now=True)

