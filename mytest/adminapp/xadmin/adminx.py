from __future__ import absolute_import
import xadmin

from . import views
from .models import UserSettings, Log
from xadmin.layout import *

from django.utils.translation import ugettext_lazy as _, ugettext

class UserSettingsAdmin(object):
    model_icon = 'fa fa-cog'
    hidden_menu = True

xadmin.site.register(UserSettings, UserSettingsAdmin)

class LogAdmin(object):

    def link(self, instance):
        if instance.content_type and instance.object_id and instance.action_flag != 'delete':
            admin_url = self.get_admin_url('%s_%s_change' % (instance.content_type.app_label, instance.content_type.model), 
                instance.object_id)
            return "<a href='%s'>%s</a>" % (admin_url, _('Admin Object'))
        else:
            return ''
    link.short_description = ""
    link.allow_tags = True
    link.is_column = False

    list_display = ('action_time', 'user', 'ip_addr', '__str__', 'link')
    list_filter = ['user', 'action_time']
    search_fields = ['ip_addr', 'message']
    model_icon = 'fa fa-cog'

xadmin.site.register(Log, LogAdmin)

class BaseSetting(object):
    enable_themes = True  # 打开主题功能
    use_bootswatch = True  # 打开可选主题库

xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSetting(object):
    site_title = "智能导航后台管理系统"     # 左上角显示信息
    site_footer = "智能导航系统"    # 最下面公司信息
    # menu_style = "accordion"    # 左侧表名按 APP 折叠

xadmin.site.register(views.CommAdminView, GlobalSetting)