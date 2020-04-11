from django.db import models

# Create your models here.
class UserProfile(models.Model):

    username = models.CharField(verbose_name="用户名", max_length=11, unique=True)
    password = models.CharField(verbose_name="密码", max_length=32)
    email = models.EmailField(verbose_name="邮箱")
    phone = models.CharField(verbose_name="手机号", max_length=11)
    is_active = models.BooleanField(verbose_name="激活状态", default=False)

    # 设置数据库中 表名
    class Meta:
        db_table = "user_user_profile"

    def __str__(self):
        return f"{self.id}--{self.username}"