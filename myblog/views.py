from django.shortcuts import render
from myblog.models import Employee
from django.template.loader import get_template
from django.http import HttpResponse
import hashlib
import re
import hashlib
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
import urllib.request
import urllib.parse


@csrf_exempt
def catalog(request):
    template = get_template('register.html')
    html = template.render(locals())
    return HttpResponse(html)


@csrf_exempt
def test(request):
    template = get_template('register.html')
    try:
        post = ""
        user_number = request.POST['account']
        user_name = request.POST['name']
        user_password = request.POST['password']
        user_phone = request.POST['phone']
        user_mail = request.POST['e-mail']
    except:
        user_number=""
        user_name = ""
        user_password = ""
        user_phone = ""
        user_mail = ""
    number_is_ok = 1
    name_is_ok = 1
    password_is_ok = 1
    phone_is_ok = 1
    mail_is_ok = 1

    if user_number!= "":
        number_pat = re.compile('^20\d{8}$')
        res = re.search(number_pat, user_number)
        if not res:
            post = "学工号格式不正确"
            number_is_ok=0
            html = template.render(locals())
            return HttpResponse(html)
        mylist = Employee.objects.all()
        for i in mylist:
            if i.number == user_number:
                post = "用户已存在"
                number_is_ok = 0
                html = template.render(locals())
                return HttpResponse(html)
    else:
        number_is_ok = 0


    if user_name != "":
        if len(user_name) > 20:
            post = "用户名过长"
            name_is_ok = 0
            html = template.render(locals())
            return HttpResponse(html)
        else:
            mylist = Employee.objects.all()
            for i in mylist:
                if i.name == user_name:
                    post = "用户名已存在"
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
            post = "密码不符合要求"
            html = template.render(locals())
            return HttpResponse(html)

    if user_phone!="":
        if not user_phone.isdigit() or len(user_phone)!=11:
            post = "手机号格式不正确"
            phone_is_ok=0
            html = template.render(locals())
            return HttpResponse(html)
        else:
            phone_pat = re.compile('^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
            res = re.search(phone_pat, user_phone)
            if not res:
                post = "手机号格式不正确"
                phone_is_ok=0
                html = template.render(locals())
                return HttpResponse(html)
    if user_mail!="":
        if not re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$",user_mail):
            post = "邮箱格式不正确"
            mail_is_ok=0
            html = template.render(locals())
            return HttpResponse(html)

    if number_is_ok == 1 and name_is_ok == 1 and password_is_ok == 1 and phone_is_ok ==1 and mail_is_ok==1:
        post = "注册成功，用户名：" + user_name
        save(user_number, user_name, user_password,user_phone,user_mail)
        return HttpResponseRedirect('/index.html')
    # else:
    #     post = ""
    print(post)
    html = template.render(locals())
    return HttpResponse(html)


def save(number, name, password, phone, mail):
    checkcode = hashlib.md5(password.encode("utf-8")).hexdigest()
    Employee.objects.create(number=number, name=name, password=checkcode, phone_number=phone, mail=mail,types="student")


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

@csrf_exempt
def index(request):
    template = get_template('index.html')
    try:
        post = ""
        user_number = request.POST['account']
        user_password = request.POST['password']
    except:
        user_number = ""
        user_password = ""
        post = ""
    login_is_ok=0

    if user_number=="":
        post = "请输入学号"
        print(250)
    else:
        mylist = Employee.objects.all()
        is_exist = 0
        correct_password=""
        for i in mylist:
            if user_number == i.number:
                is_exist = 1
                correct_password = i.password
                break
        if is_exist == 0:
            post = "用户不存在"
        else:
            if user_password == "":
                post = "请输入密码"
            else:
                checkcode = hashlib.md5(user_password.encode("utf-8")).hexdigest()
                print(checkcode)
                print("\n")
                print(correct_password)
                if checkcode == correct_password:
                    post = "登陆成功"
                    return HttpResponseRedirect('/homepage/main.html')
                else:
                    post = "密码错误"
    html = template.render(locals())
    return HttpResponse(html)


def homepage(request):
    template = get_template('main.html')
    html = template.render(locals())
    return HttpResponse(html)


def homepage_deal(request, url):
    template = get_template(url)
    html = template.render(locals())
    return HttpResponse(html)
    # return HttpResponseRedirect(url)
    # print("hhh")
    # print(str(url))
    # template = get_template('main.html')
    # html = template.render(locals())
    # return HttpResponse(html)


def register(request):
    template = get_template('register.html')
    html = template.render(locals())
    return HttpResponse(html)


def reset(request):
    template = get_template('reset.html')
    html = template.render(locals())
    return HttpResponse(html)


@csrf_exempt
def login_tsinghua(request):
    user_name = request.POST.get('account')
    password = request.POST.get('password')
    my_arguments = urllib.parse.urlencode({'userid': user_name,
                                           'userpass': password}).encode(encoding='UTF-8')
    learn_tsinghua_url = 'https://learn.tsinghua.edu.cn/MultiLanguage/lesson/teacher/loginteacher.jsp'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0', }
    my_request = urllib.request.Request(url=learn_tsinghua_url,
                                        headers=headers,
                                        data=my_arguments,
                                        method='POST')
    login_result = urllib.request.urlopen(my_request).read().decode('UTF-8')
    post = ""
    if login_result.find('用户名或密码错误') != -1:
        post = '用户名或密码错误，登录失败'
    elif login_result.find('没有登陆网络学堂的权限') != -1:
        post = '您没有登陆权限！请确认是清华教工或学生！'
    else:
        post = '验证成功'
    #print(login_result)
    template = get_template('index.html')
    html = template.render(locals())

    return HttpResponse(html)
