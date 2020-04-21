from django.db import models

from goods.models import SKU
from tools.models import BaseModel
from user.models import UserProfile

STATUS = (
    (1, "待付款"),
    (2, "待发货"),
    (3, "待收货"),
    (4, "已完成"),
)


class OrderInfo(BaseModel):

    order_id = models.CharField(verbose_name="订单编号", max_length=64, primary_key=True)
    user = models.ForeignKey(UserProfile) # ??
    total_count = models.IntegerField(verbose_name="商品总数", default=1)
    total_amount = models.DecimalField(verbose_name="商品总金额", max_digits=10, decimal_places=2)
    freight = models.DecimalField(verbose_name="运费", max_digits=10, decimal_places=2)
    pay_method = models.SmallIntegerField(verbose_name="支付方式", default="1") # ??

    # 订单地址
    receiver = models.CharField(verbose_name="收件人", max_length=10)
    # 理论上应该拆分成　省　县　乡　具体地址
    address = models.CharField(verbose_name="用户地址", max_length=100)
    receiver_mobile = models.CharField(verbose_name="收件人联系电话", max_length=11)
    tag = models.CharField(verbose_name="标签", max_length=10)

    # choices 选项可将该字段在admin后台中　显示为下拉列表
    status = models.SmallIntegerField(verbose_name="订单状态", choices=STATUS)


    class Meta:
        db_table = "order_order_info"

    def __str__(self):
        return self.order_id



class OrderGoods(BaseModel):

    order_info = models.ForeignKey(OrderInfo)
    sku = models.ForeignKey(SKU)
    count = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "order_order_goods"

    def __str__(self):
        return self.sku.name

