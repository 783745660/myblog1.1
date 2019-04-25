#coding=utf-8
__author__ = 'CoderSong'
__date__ = '2019/4/23 13:34'

import xadmin
from .models import Comment


class CommentsAdmin(object):
    list_display = ['name','email','article','comment_time']

xadmin.site.register(Comment,CommentsAdmin)