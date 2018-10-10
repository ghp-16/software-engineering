from django.shortcuts import render
from myblog.models import Employee
from django.template.loader import get_template
from django.http import HttpResponse
import hashlib


# def test(request):
#     # test1 = Employee(name="yc")
#     # test1.save()
#     # save('yc')
#     # mylist = Employee.objects.all()
#     # for i in mylist:
#     #     print(i.name)
#     template = get_template('index.html')
#     try:
#         post = str(request.POST)
#         user_name = request.GET['user_name']
#         user_mail = request.GET['user_mail']
#     except:
#         user_name = ""
#         user_mail = ""
#     checkcode = hashlib.md5(user_mail.encode("utf-8")).hexdigest()
#     post = "你提交的内容是：" + "姓名：" + user_name + "邮箱："+ checkcode
#     if user_name == "" or user_mail == "":
#         post = ""
#     else:
#         save(user_name)
#     html = template.render(locals())
#     return HttpResponse(html)
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
        user_name = request.GET['account']
        user_password = request.GET['password']
    except:
        user_name = ""
        user_password = ""
    name_judge = "请输入用户名，由汉字、字母、数字、字符组成，长度不超过20"
    password_judge = "请输入密码，由字母、数字、字符组成，且至少包含两种，长度为8-20"
    name_is_ok = 1;
    password_is_ok = 1;
    if user_name != "":
        if len(user_name) > 20:
            post = ""
            name_is_ok = 0
            html = template.render(locals())
            return HttpResponse(html)
        else:
            mylist = Employee.objects.all()
            for i in mylist:
                if i.name == user_name:
                    name_judge = "用户名已存在"
                    post = ""
                    name_is_ok = 0
                    html = template.render(locals())
                    return HttpResponse(html)

    else:
        name_is_ok = 0;
    if user_password != "":
        digit = 0
        alpha = 0
        zifu = 0
        for item in user_password:
            if item.isdigit():
                digit = 1
            elif item.isalpha():
                alpha = 1
            else:
                zifu = 1;
        if digit + alpha + zifu <= 1 or len(user_password) < 8 or len(user_password) > 20:
            password_is_ok = 0
            password_judge = "密码不符合要求（由字母、数字、字符组成，且至少包含两种，长度为8-20）"

            html = template.render(locals())
            return HttpResponse(html)
    if name_is_ok == 1 and password_is_ok == 1:
        post = "注册成功，用户名：" + user_name
        save(user_name, user_password)
    else:
        post = ""
    html = template.render(locals())
    return HttpResponse(html)


def save(name,password):
    Employee.objects.create(name=name,password=password)


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


def index(request):
    template = get_template('index.html')
    html = template.render(locals())
    return HttpResponse(html)


def register(request):
    template = get_template('register.html')
    html = template.render(locals())
    return HttpResponse(html)


def reset(request):
    template = get_template('reset.html')
    html = template.render(locals())
    return HttpResponse(html)