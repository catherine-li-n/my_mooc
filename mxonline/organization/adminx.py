# -*- coding:utf-8 -*-
__author__ = 'catherine'
__date__ = '2019/3/14 9:30 AM'
import xadmin
from .models import CityDict, CourseOrg, Teacher

class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums','fav_nums','image','address','city']
    search_fields = ['name', 'desc', 'click_nums','fav_nums','image','address','city']
    list_filter = ['name', 'desc', 'click_nums','fav_nums','image','address','city']


class TeacherAdmin(object):
    list_display = ['name', 'click_nums', 'work_years', 'work_company', 'work_position', 'add_time']
    search_fields = ['name', 'click_nums', 'work_years', 'work_company', 'work_position']
    list_filter =['name', 'click_nums', 'work_years', 'work_company', 'work_position', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
