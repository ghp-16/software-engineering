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
from django.views.static import serve
from . import settings

urlpatterns = [
    #________________page link ______________   
    path('', myblog.views.login_tsinghua),
    # path('index.html', myblog.views.index),
    path('index.html', myblog.views.login_tsinghua),
    path('tsinghua/', myblog.views.login_tsinghua),
    path('check_in_index/', myblog.views.checkin_index),
    path('tsinghua_login/', myblog.views.tsinghua),
    path('homepage/manage_student.html', myblog.views.manage_type),
    # path('homepage/form_edit.html', myblog.views.form_edit),
    path('homepage/manage_team.html', myblog.views.manage_team),
    path('homepage/interview_edit.html', myblog.views.interview_edit),
    path('homepage/sign_up_interview.html', myblog.views.sign_up_interview),
    path('homepage/manage_interview.html', myblog.views.manage_interview),
    path('homepage/send_txt.html', myblog.views.manage_send_txt),
    path('homepage/notice.html', myblog.views.manage_notice),
    path('homepage/judge_interview.html', myblog.views.judge_interview),
    path('homepage/judge_interview/', myblog.views.judge_interview),
    path('homepage/checkin/', myblog.views.checkin),
    # path('index.html', myblog.views.login_tsinghua),
    path('test/', myblog.views.test),
    # path('query/', myblog.views.query),
    path('reset.html', myblog.views.reset),
    path('register.html', myblog.views.test),
    path('homepage/', myblog.views.homepage),
    path('homepage/manage_signup.html', myblog.views.sign_up),

    #______________function link______________________
    url(r'.+\/get_qrcode/',myblog.views.get_qrcode),
    url(r'.+\/get_interview_students/', myblog.views.get_interview_students),
    url(r'.+\/check_in_interview/', myblog.views.check_in_interview),
    url(r'.+\/get_interview_info/', myblog.views.get_interview_info),
    url(r'.+\/set_student/',myblog.views.set_student),
    url(r'.+\/delMem/',myblog.views.del_mem),
    url(r'.+\/delteam/',myblog.views.del_team),
    url(r'.+\/del_choose/',myblog.views.del_choose),
    url(r'.+\/get_choose/',myblog.views.get_choose),
    url(r'.+\/modify_info/', myblog.views.modify_info),
    url(r'.+\/manage_info/', myblog.views.get_student_info),
    url(r'.+\/new_interview/', myblog.views.new_interview),
    url(r'.+\/del_interview/', myblog.views.del_interview),
    url(r'.+\/set_open/', myblog.views.set_open),
    url(r'.+\/notice/',myblog.views.notice),
    url(r'.+\/send_txt/',myblog.views.send_txt),
    url(r'.+\/left.html', myblog.views.homepage_info),
    url(r'.+\/left_team.html', myblog.views.homepage_info),
    url(r'.+\/left_judge.html', myblog.views.homepage_info),
    url(r'.+\/left_web.html', myblog.views.homepage_info),
    url(r'.+\/add_student/', myblog.views.add_student),
    url(r'.+\/del_student/', myblog.views.del_student),
    url(r'.+\/create_form/', myblog.views.create_form),
    url(r'.+\/form_edit/', myblog.views.form_edit),
    # path('homepage/form_edit.html', myblog.views.form_edit),

    url(r'homepage/(.+)',  myblog.views.homepage_deal),
    # path('homepage/left.html', myblog.views.homepage_deal),
    # path('homepage/student.html', myblog.views.homepage_deal),
    path('admin/', admin.site.urls),
    path('catalog/', myblog.views.catalog),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]

urlpatterns += staticfiles_urlpatterns()