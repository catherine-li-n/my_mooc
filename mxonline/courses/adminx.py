# -*- coding:utf-8 -*-
import xadmin

__author__ = 'catherine'
__date__ = '2019/3/13 11:12 PM'

from .models import Course,Lesson,Video,CourseResource


class CourseAdmin(object):

    list_display = ['name','desc','detail', 'degree','learn_times',
                    'student','fav_nums','image','click_nums','add_time']
    search_fileds = ['name', 'desc', 'detail', 'degree','students']
    list_filter = ['name','desc','detail','degree','learn_times',
                    'student','fav_nums','image','click_nums','add_time']
    ordering = ['-click_nums']


class LessonAdmin(object):
    list_display = ['course','name', 'add_time']
    search_fileds =['course','name']
    list_filter = ['course__name','name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fileds = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fileds = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']

xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)