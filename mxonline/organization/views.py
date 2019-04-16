# -*- coding:utf-8 -*-
import json

from pure_pagination import Paginator, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import View

from operation.models import UserFavorite
from .models import CourseOrg, CityDict, Teacher
from .forms import UserAskForm
from django.http import HttpResponse
from courses.models import Course

# Create your views here.
class OrgView(View):
    """
    课程机构
    """
    def get(self, request):
        #课程机构
        all_orgs = CourseOrg.objects.all()
        org_nums = all_orgs.count()
        hot_orgs = all_orgs.order_by("click_nums")[:3]
        #城市筛选
        all_citys = CityDict.objects.all()
        #课程搜索
        search_keywords = request.GET.get("keywords","")
        if search_keywords:
            all_orgs = all_orgs.filter(Q(name__icontains=search_keywords)|Q(desc__icontains=search_keywords))

        city_id = request.GET.get('city',"")
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))
        #类别筛选
        category = request.GET.get('ct',"")
        if category:
            all_orgs = all_orgs.filter(category=category)

        sort = request.GET.get('sort',"")
        if sort:
            if sort == "students":
                all_orgs = all_orgs.order_by("-students")
            elif sort == "course_nums":
                all_orgs = all_orgs.order_by("-course_nums")

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)

        return render(request, "org-list.html", {
            "city_id":city_id,
            "all_orgs":orgs,
            "all_citys":all_citys,
            "org_nums":org_nums,
            "category":category,
            "hot_orgs":hot_orgs,
            "sort":sort,
        })

class AddUserAskView(View):
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.valid():
            user_ask = userask_form.save(commit=True)
            return HttpResponse("{'status':'success'}",content_type='application/json')
        else:
            return HttpResponse("{'status':'fail','msg':{0}}".format(userask_form.errors))

class OrgHomeView(View):
    def get(self,request,org_id):
        current_org= CourseOrg.objects.get(id=(org_id))
        course_org = CourseOrg.objects.get(id = int(org_id))
        course_org.click_nums +=1
        course_org.save()
        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                    has_fav = True
        all_courses = course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:1]
        return render(request, 'org-detail-homepage.html',{
            'all_course': all_courses,
            'all_teacher': all_teachers,
            'course_org': course_org,
            'current_page':current_org,
            'has_fav':has_fav,
            'org_id': org_id,
        })


class OrgCourseView(View):
    def get(self,request,org_id):
        current_page = 'course'

        course_org = CourseOrg.objects.get(id = int(org_id))
        all_courses = course_org.course_set.all()
        return render(request, 'org-detail-course.html',{
            'all_course': all_courses,
            'course_org':course_org,
            'current_page':current_page
        })


class OrgDescView(View):
    def get(self,request,org_id):
        current_page = 'desc'
        course_org = CourseOrg.objects.get(id = int(org_id))
        all_courses = course_org.course_set.all()
        return render(request, 'org-detail-desc.html',{
            'course_org':course_org,
            'current_page':current_page
        })

class OrgTeacherView(View):
    def get(self, request, org_id):
        current_page = 'teacher'
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_teachers = course_org.teacher_set.all()
        return render(request, 'org-detail-teachers.html', {
            'all_teachers':all_teachers,
            'course_org': course_org,
            'current_page': current_page
        })

class AddFavView(View):
    def set_fav_nums(self, fav_type, fav_id, num=1):
        if fav_type == 1:
            course = Course.objects.get(id=fav_id)
            course.fav_nums += num
            course.save()
        elif fav_type == 2:
            course_org = CourseOrg.objects.get(id=fav_id)
            course_org.fav_nums += num
            course_org.save()
        elif fav_type == 3:
            teacher = Teacher.objects.get(id=fav_id)
            teacher.fav_nums += num
            teacher.save()

    def post(self, request):
        fav_id = int(request.POST.get('fav_id', 0))
        fav_type = int(request.POST.get('fav_type', 0))

        res = dict()
        if not request.user.is_authenticated:
            res['status'] = 'fail'
            res['msg'] = '用户未登录'
            return HttpResponse(json.dumps(res), content_type='application/json')

        # 查询收藏记录
        exist_records = UserFavorite.objects.filter(user=request.user, fav_id=fav_id, fav_type=fav_type)
        if exist_records:
            exist_records.delete()
            self.set_fav_nums(fav_type, fav_id, -1)
            res['status'] = 'success'
            res['msg'] = '收藏'
        else:
            user_fav = UserFavorite()
            if fav_id and fav_type:
                user_fav.user = request.user
                user_fav.fav_id = fav_id
                user_fav.fav_type = fav_type
                user_fav.save()
                self.set_fav_nums(fav_type, fav_id, 1)

                res['status'] = 'success'
                res['msg'] = '已收藏'
            else:
                res['status'] = 'fail'
                res['msg'] = '收藏出错'
        return HttpResponse(json.dumps(res), content_type='application/json')



class TeacherListView(View):
    """
    课程讲师列表页
    """
    def get(self, request):
        all_teachers = Teacher.objects.all()
        current_nav = "teacher"
        search_keywords = request.GET.get("keywords", "")
        if search_keywords:
            all_teachers = all_teachers.filter(Q(name__icontains=search_keywords) |
                                               Q(work_company__icontains=search_keywords) |
                                               Q(work_position__icontains=search_keywords))
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "click_nums":
                all_teachers = all_teachers.order_by("-click_nums")

        sorted_teacher = Teacher.objects.all().order_by("-click_nums")[:3]
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_teachers, 3, request=request)
        teachers = p.page(page)
        return render(request, "teachers-list.html", {
            "all_teachers":teachers,
            "sorted_teacher":sorted_teacher,
            "sort":sort,
            "current_nav":current_nav
        })


class TeacherDetailView(View):
    def get(self, request, teacher_id):
        teacher = Teacher.objects.get(id=int(teacher_id))
        teacher.click_nums += 1
        teacher.save()

        all_courses = Course.objects.filter(teacher=teacher)

        has_teacher_faved =False
        if UserFavorite.objects.filter(user=request.user, fav_type = 3, fav_id = teacher.id):
            has_teacher_faved = True

        has_org_faved = False
        if UserFavorite.objects.filter(user=request.user, fav_type = 2, fav_id = teacher.org_id):
            has_org_faved = True

        sorted_teacher = Teacher.objects.all().order_by("-click_nums")[:3]
        return render(request, "teacher-detail.html", {
            "teacher": teacher,
            "all_courses": all_courses,
            "sorted_teacher": sorted_teacher,
            "has_teacher_faved": has_teacher_faved,
            "has_org_faved": has_org_faved
        })