from django.contrib import admin

# Register your models here.
# from TestModel.models import Test, Contact, Tag


# Register your models here.
from userapp.models import User


# class TagInline(admin.TabularInline):
#     model = User


class UserAdmin(admin.ModelAdmin):
    list_display = ['u_id', 'u_name', 'u_email', 'u_password', 'is_delete']
    search_fields = ['t_id', 't_name', 'u_email']
    list_filter = ['u_id', 'u_name', 'u_email', 'u_password', 'is_delete']
    list_per_page = 20
    # readonly_fields = ['t_id', 't_name']
    refresh_times = [10, 20, 30, 60]
    list_export = ('xls', 'xml', 'json')
    list_export_fields = ('u_id', 'u_name', 'u_email')
    model_icon = 'fa fa-user'

admin.site.register(User, UserAdmin)

admin.site.site_title = "智能出行导航系统--后台管理"
admin.site.site_header = "智能出行导航系统"
admin.site.index_title = "后台主页"