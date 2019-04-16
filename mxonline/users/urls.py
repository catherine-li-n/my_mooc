# -*- coding:utf-8 -*-
__author__ = 'catherine'
__date__ = '2019/3/19 11:01 AM'

from django.conf.urls import url
from django.urls import include
from .views import UserinfoView,UploadImageView,UpdatePwdView,SendEmailCodeView\
                  ,UpdateEmailView,MyCourseView,MyFavOrgView,MyFavTeacherView,MyFavCourseView,MymessageView
app_name ='[users]'

urlpatterns =[
    #用户信息
    url(r'^info/$', UserinfoView.as_view(), name="user_info"),
    #用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),
    #用户个人中心修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),
    #用户个人中心修改邮箱
    url(r'^sendemail_code/pwd/$', SendEmailCodeView.as_view(), name="sendemail_code"),
    #用户个人中心修改邮箱
    url(r'^update_email/pwd/$', UpdateEmailView.as_view(), name="update_email"),
    #我的课程
    url(r'^mycourse/$', MyCourseView.as_view(), name="mycourse"),
    #我的课程机构
    url(r'^myfav/org/$', MyFavOrgView.as_view(), name="myfav_org"),
    #我的授课讲师
    url(r'^myfav/teacher/$', MyFavTeacherView.as_view(), name="myfav_teacher"),
    #我的收藏的课程
    url(r'^myfav/course/$', MyFavCourseView.as_view(), name="myfav_course"),
    #我的消息
    url(r'^mymessage/$', MymessageView.as_view(), name="mymessage"),

]