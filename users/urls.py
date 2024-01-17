"""为应用程序users定义URL模式"""

#from django.conf.urls import url
from django.urls import re_path as url #上面旧版的不再用
#from django.conf.auth.views import login
from django.contrib.auth.views import LoginView #上面老版本不用

from . import views

urlpatterns = [
    #登录页面
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    #注销
    url(r'^logout/$', views.logout_view, name='logout'),
    #注册页面
    url(r'^register/$', views.register, name='register')
]
