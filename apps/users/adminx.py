import xadmin

from .models import EmailVerifyRecord,Banner
from xadmin import views

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSetting(object):
    site_title = "教育后台管理系统"
    site_footer = "教育在线"
    menu_style = "accordion"

class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_type','send_time']
    search_fields = ['code','email','send_type','send_time']
    list_filter = ['code','email','send_type','send_time']   # 过滤功能

class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index','add_time']
    search_fields = ['title', 'image', 'url', 'index','add_time']
    list_filter = ['title', 'image', 'url', 'index','add_time']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)