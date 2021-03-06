# _*_ coding: utf-8 _*_
__author__ = 'amy'
__date__ = '18-6-8 下午3:04'
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=5)
    password = forms.CharField(required=True)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=5)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


class FindPasswordForm(forms.Form):
    password = forms.CharField(required=True, min_length=6,max_length=20)
    password2 = forms.CharField(required=True, min_length=6,max_length=20)

