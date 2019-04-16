# -*- coding:utf-8 -*-
from .views import *
__author__ = 'catherine'
__date__ = '2019/3/17 11:03 AM'


from django.conf.urls import url
from django.urls import include
app_name ='[courses]'
urlpatterns =[
    url(r'^list/$', CourseListView.as_view(), name="course_list"),
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),
    url(r'^info/(?P<course_id>\d+)/$',CourseInfoView.as_view(), name="course_info"),
    # 评论页面
    url(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name='course_comment'),
    # 添加课程评论
    url(r'^add_comment/$', AddCommentsView.as_view(), name='add_comment'),
    #
    url(r'^video/(?P<video_id>\d+)/$', CourseDetailView.as_view(), name="video_play")

]