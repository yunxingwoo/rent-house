from django import forms
from django.contrib.auth.models import User
from workapp.models import UserInfo
from workapp.models import UserInfo,HouseInfo,Area

import re
from django.core.exceptions import ValidationError

def email_test(email):
    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) == None:
        raise ValidationError(u"邮箱格式不正确")

def username_test(username):
    if len(username) > 14:
        raise ValidationError(u"请输入14字以内的用户名")

def username_rename(username):
	try:
		User.objects.get(username=username)
	except User.DoesNotExist:
		return username
	raise ValidationError(u"用户名被占用")


def password_test(password):
    if len(password) < 6:
        raise ValidationError(u"请输入6位以上的密码")

def check_passwords(passowrd):
    user = User.objects.all()
    if user.password != password:
        raise ValidationError(u'密码错误')

def check_email(email):
    user = User.objects.all().filter(email=email)
    print(user)
    if email != UserInfo.email:
        raise ValidationError(u'邮箱输错了')

def check_password(password):
    if password != UserInfo.password:
        raise ValidationError(u'密码输错了')

class UserForm(forms.Form):
    email = forms.EmailField(label=u'邮箱',validators=[email_test])
    username = forms.CharField(label=u'用户名',max_length=100,validators=[username_test,username_rename],error_messages={'required': u'你这个无名人士.....'})
    password = forms.CharField(label=u'密码',widget=forms.PasswordInput(),validators=[password_test,check_passwords])

class LoginForm(forms.Form):
    email = forms.EmailField(label=u'邮箱',max_length=100)
    password = forms.CharField(label=u'密码',widget=forms.PasswordInput())



class ModifyUserForm(forms.Form):
    username = forms.CharField(label=u'修改用户名',max_length=100)
    password = forms.CharField(label=u'修改密码',widget=forms.PasswordInput())
