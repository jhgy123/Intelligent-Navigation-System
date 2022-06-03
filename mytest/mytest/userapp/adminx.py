from asyncio.log import logger
from hashlib import md5

import xlrd as xlrd
from django.apps import apps
from django.contrib.auth.hashers import make_password
import xadmin
# from xadmin.plugins.excel import excel_into_model

from userapp.models import User


class UserAdmin(object):
    list_display = ['u_id', 'u_name', 'u_email', 'u_password', 'is_delete']
    search_fields = ['t_id', 't_name', 'u_email']
    list_filter = ['u_id', 'u_name', 'u_email', 'u_password', 'is_delete']
    list_per_page = 20
    # readonly_fields = ['t_id', 't_name']
    refresh_times = [10, 20, 30, 60]
    list_export = ('xls', 'xml', 'json')
    list_export_fields = ('u_id', 'u_name', 'u_email')
    model_icon = 'fa fa-user'

xadmin.site.register(User, UserAdmin)


