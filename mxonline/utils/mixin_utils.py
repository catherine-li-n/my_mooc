# -*- coding:utf-8 -*-
__author__ = 'catherine'
__date__ = '2019/3/17 5:12 PM'

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
class LoginRequiredMixin(object):

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self,request, *args,**kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)