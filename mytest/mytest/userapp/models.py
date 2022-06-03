from django.db import models

# Create your models here.

class User(models.Model):
    u_id = models.CharField('手机号', max_length=11, primary_key=True, unique=True)
    u_name = models.CharField('姓名', max_length=32)
    u_email = models.CharField('邮箱', max_length=64)
    u_password = models.CharField('密码', max_length=256)
    is_delete = models.BooleanField('账号是否已删除', default=False)

    class Meta:
        db_table = 'user_table'
        verbose_name = u'用户详细信息'
        verbose_name_plural = verbose_name