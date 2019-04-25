#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称', default='')  # 昵称
    birday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(max_length=20, choices=(('male', u'男'), ('female', '女')), default='female')
    address = models.CharField(max_length=100, verbose_name=u'地址', default=u'')
    phonenumber = models.CharField(max_length=11, null=True, blank=True)

    class Meta:
        '''定义表的Meta信息
        '''
        #定义在管理后台显示的名称
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username  # 因为我们已经继承了AbstractUser,而这里的username在AbstractUser这个类中