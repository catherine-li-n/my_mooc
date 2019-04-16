# -*- coding:utf-8 -*-
from random import Random

from django.core.mail import send_mail

from mxonline.settings import EMAIL_FROM

__author__ = 'catherine'
__date__ = '2019/3/14 3:48 PM'

from users.models import EmailVerifyRecord

def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhLlIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890'
    length = len(chars)-1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0,length)]
    return str

def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""
    if send_type == "register":
        email_title = "『ARASHI Anniversary Tour 5×20』抽選結果のお知らせ"
        email_body = "Please click:http://127.0.0.1:8000/active/{0}".format(code)

        send_status = send_mail(email_title, email_body,EMAIL_FROM,[email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "おめでとうございます！第4希望で当選です。"
        email_body = "Please click:http://127.0.0.1:8000/reset/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "update_email":
        email_title = "おめでとうございます！第1希望で当選です。"
        email_body = "Please click:http://127.0.0.1:8000/reset/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
