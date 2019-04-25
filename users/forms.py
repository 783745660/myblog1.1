#coding=utf-8
__author__ = 'CoderSong'
__date__ = '2019/4/23 14:19'

from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import UserProfile


#定义一个用户注册表单
class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):  # Meta内部类下的model属性对应的是auth.User模型，通过类的复写，将其改为users.UserProfile
        model = UserProfile
        fields = ('username','email')


#定义一个登录验证表单
class LoginForm(forms.Form):
    username = forms.CharField(required=True,min_length=3)  #用户名不为空，至少3个字符串
    password = forms.CharField(required=True,min_length=5)  #密码不能为空，至少5个字符串
