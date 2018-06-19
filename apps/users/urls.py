# _*_ coding: utf-8 _*_
__author__ = 'amy'
__date__ = '18-6-8 上午10:21'
from django.conf.urls import url
from .views import index, LoginView, RegisterView, ActiveEmailView, reActiveEmail, myMail

urlpatterns = [
    url(r'^index/$', index, name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^user/active/(?P<code>.*)/$', ActiveEmailView.as_view(), name='active'),
    url(r'^resend_email/$', reActiveEmail, name='reactive'),
    url(r'^my_mail/$', myMail)
]