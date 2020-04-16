from django.db import models

class BaseModel(models.Model):
    # 抽象模型类，用于继承通用字段
    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        # 指定当前模型类为　抽象模型类
        abstract = True


