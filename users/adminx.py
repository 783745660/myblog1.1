#coding=utf-8
__author__ = 'CoderSong'
__date__ = '2019/4/23 13:12'
import xadmin
from  xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = '博客管理系统'
    site_footer = '博客之家'
    menu_style = 'accordion'


xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)