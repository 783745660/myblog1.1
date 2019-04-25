#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from django.contrib.auth import authenticate,login  #用于用户登录是的验证和登录
from .forms import LoginForm,RegisterForm
from  blog.models import Article


# Create your views here.

'''定义用户注册视图函数'''
class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        return render(request,'users/register.html',{'register_form':register_form})

    def post(self,request):
        register_form = RegisterForm(request.POST)
        print register_form.errors

        if register_form.is_valid():
            register_form.save()

            return render(request,'registration/login.html')

        else:
            return render(request,'users/register.html',{'register_form':register_form})



'''这里定义用户登录视图类，该类继承View,View用于处理登录和退出
'''

# class LoginView(View):
#     #http方法为get
#     def get(self,request):
#         login_form = LoginForm()
#         return render(request,'users/login.html',{'login_form':login_form}) #如果用户是get方法登录，那么页面直接跳转到bolg下的login.html页面
#
#     #http方法为post，携带用户数据
#     def post(self,request):
#         login_form = LoginForm(request.POST)        # 实例化一个表单对象
#         print login_form.errors                     # 有错误就输出错误
#
#         if login_form.is_valid():
#             user_name = request.POST.get('username','')
#             pass_word = request.POST.get('password','')
#             user = authenticate(user_name=user_name,pass_word=pass_word) #得到用户的表单输入，若合法，返回一个user对象
#
#             if user is not None:
#                 '''如果存在该用户，则登录完成，返回博客主页'''
#                 login(request,user)
#                 request.session['user'] = user_name
#                 return HttpResponse('登录成功')
#
#                     # article_list = Article.objects.all()
#                     # latest_article_list = Article.objects.all()
#                     #
#                     # return render(request,'blog/index.html',{'article_list':article_list,
#                     #                                          'latest_article_list':latest_article_list})
#
#             else:
#                 return render(request,'users/login.html',{'msg': '用户名或密码错误'})
#
#         else:
#             return render(request,'users/login.html',{'login_form':login_form})

class ForgetPwdView(View):
    pass




