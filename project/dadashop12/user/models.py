from django.db import models

# Create your models here.
class UserProfile(models.Model):

    username = models.CharField(verbose_name="用户名", max_length=11, unique=True)
    password = models.CharField(verbose_name="密码", max_length=32)
    email = models.EmailField(verbose_name="邮箱")
    phone = models.CharField(verbose_name="手机号", max_length=11)
    is_active = models.BooleanField(verbose_name="激活状态", default=False)
    created_time = models.DateTimeField(auto_now_add=True) # 创建时间
    update_time = models.DateTimeField(auto_now=True) # 更新时间

    # 设置数据库中 表名
    class Meta:
        db_table = "user_user_profile"

    def __str__(self):
        return f"{self.id}--{self.username}"

class Address(models.Model):

    user_profile = models.ForeignKey(UserProfile)
    receiver = models.CharField(verbose_name="收件人姓名", max_length=11)
    address = models.CharField(max_length=100, verbose_name="用户地址")
    is_default = models.BooleanField(verbose_name="是否为默认地址", default=False)
    is_active = models.BooleanField(verbose_name="是否使用", default=True)
    postcode = models.CharField(verbose_name="邮编", max_length=6)
    receiver_mobile = models.CharField(verbose_name="收件人电话", max_length=11)
    tag = models.CharField(verbose_name="标签", max_length=10)
    created_time = models.DateTimeField(auto_now_add=True) # 创建时间
    update_time = models.DateTimeField(auto_now=True) # 更新时间

class WeiboProfile(models.Model):

    user_profile = models.OneToOneField(UserProfile, null=True)
    wuid = models.CharField(verbose_name="微博uid", max_length=10, unique=True)
    access_token = models.CharField(verbose_name="权限令牌", max_length=32)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_weibo_profile"

    def __str__(self):
        return self.wuid



