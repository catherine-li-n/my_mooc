# -*- coding:utf-8 -*-
from __future__  import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"nickname", default="")
    birthday = models.DateField(verbose_name=u"birth", null=True, blank=True)
    gender = models.CharField(max_length=7, choices=(("male",u"男"),('female',u"女")), default='female')
    address = models.CharField(max_length=100, default=u"")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y/%m', default=u'image/default.png')


    class Meta:
        verbose_name = "user info"
        verbose_name_plural = verbose_name

    def unread_nums(self):
        #获取用户未对消息的数量
        from operation.models import UserMessage
        return UserMessage.objects.filter(user=self.id, has_read=False).count()


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"valid code")
    email = models.EmailField(max_length=50, verbose_name=u"email")
    send_type = models.CharField(choices=(("register","注册"),("forget",u"找回密码"),("email_update",u"修改邮箱")), max_length=30)
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)

class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"title")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name=u"scroll", max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name


