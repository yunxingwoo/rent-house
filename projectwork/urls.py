"""projectwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth.views import logout,login
from django.conf import settings
from workapp.views import *


urlpatterns = [
    #后台管理系统
    url(r'^admin/', admin.site.urls),
    #index页
    url(r'^index/$',index,name='index'),
    #列表页
    url(r'^list/$', list, name='list'),
    #详情页
    url(r'^detail/(?P<id>\d+)$', detail, name='detail'),
    #用户信息
    url(r'^userinfo/$', userinfo, name='userinfo'),
    #登陆
    url(r'^login/$', login, name='login'),
    #注册
    url(r'^register/$', register, name='register'),
    #修改信息
    url(r'^alteruser/$', alteruser, name='alteruser'),
    #提交预约
    url(r'^appointment/$', appointment, name='appointment'),
    #登出
    url(r'^logout/$', logout, {'next_page': '/register'}, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
