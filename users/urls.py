#coding=utf-8
__author__ = 'CoderSong'
__date__ = '2019/4/23 16:22'

from django.conf.urls import url,include
from .views import ForgetPwdView,RegisterView

app_name = 'users'
urlpatterns = [
    # url(r'^login/',LoginView.as_view(),name='login'),
    url(r'^register/$',RegisterView.as_view(),name='register'),
    url(r'^forget/$',ForgetPwdView.as_view(),name='forget_pwd'),
]