from django.shortcuts import render
from myblog.models import Employee
from django.template.loader import get_template
from django.http import HttpResponse
import hashlib


def test(request):
    # test1 = Employee(name="yc")
    # test1.save()
    # save('yc')
    # mylist = Employee.objects.all()
    # for i in mylist:
    #     print(i.name)
    template = get_template('index.html')
    try:
        post = str(request.POST)
        user_name = request.GET['user_name']
        user_mail = request.GET['user_mail']
    except:
        user_name = ""
        user_mail = ""
    checkcode = hashlib.md5(user_mail.encode("utf-8")).hexdigest()
    post = "你提交的内容是：" + "姓名：" + user_name + "邮箱："+ checkcode
    if user_name == "" or user_mail == "":
        post = ""
    else:
        save(user_name)
    html = template.render(locals())
    return HttpResponse(html)


def save(name):
    Employee.objects.create(name=name)


def query(request):
    template = get_template('query.html')
    try:
        post = str(request.POST)
        user_name = request.GET['user_name']
    except:
        user_name = ""

    mylist = Employee.objects.all()
    post = "查询结果："
    if user_name == "":
        for i in mylist:
            post += i.name + ","
    else:
        is_exist = False
        for i in mylist:
            if user_name == i.name:
                is_exist = True
                break
        if is_exist:
            post += "该用户存在"
        else:
            post += "该用户不存在"
    html = template.render(locals())
    return HttpResponse(html)
# Create your views here.


