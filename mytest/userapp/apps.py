from django.apps import AppConfig


class UserappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userapp'
    verbose_name = "用户信息管理" #改变显示标签的内容为"用户"
