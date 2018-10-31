"""DjangoMySQLDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
import myblog.views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles

urlpatterns = [
    #________________page link ______________   
    path('', myblog.views.index),
    path('index.html', myblog.views.index),
    path('tsinghua/', myblog.views.login_tsinghua),
    path('homepage/manage_student.html', myblog.views.manage_type),
    path('homepage/manage_team.html', myblog.views.manage_team),
    path('homepage/interview_edit.html', myblog.views.interview_edit),
    # path('index.html', myblog.views.login_tsinghua),
    path('test/', myblog.views.test),
    # path('query/', myblog.views.query),
    path('reset.html', myblog.views.reset),
    path('register.html', myblog.views.test),
    path('homepage/', myblog.views.homepage),
    path('homepage/manage_signup.html', myblog.views.sign_up),

    #______________function link______________________
    url(r'.+\/set_student/',myblog.views.set_student),
    url(r'.+\/delMem/',myblog.views.del_mem),
    url(r'.+\/delteam/',myblog.views.del_team),
    url(r'.+\/delChoose/',myblog.views.del_choose),
    url(r'.+\/getChoose/',myblog.views.get_choose),
    url(r'.+\/modify_info/', myblog.views.modify_info),
    url(r'.+\/manage_info/', myblog.views.get_student_info),
    url(r'.+\/new_interview/', myblog.views.new_interview),


    url(r'homepage/(.+)',  myblog.views.homepage_deal),
    # path('homepage/left.html', myblog.views.homepage_deal),
    # path('homepage/student.html', myblog.views.homepage_deal),
    path('admin/', admin.site.urls),
    path('catalog/', myblog.views.catalog),
]

urlpatterns += staticfiles_urlpatterns()