from django.shortcuts import render
from myblog.models import Employee, Team, Interview
from django.template.loader import get_template
from django.forms.models import model_to_dict
from django.http import HttpResponse
import re
import hashlib
import json
import time
from myblog.qrcode_producer import produce_qrcode
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
import urllib.request
import urllib.parse
import http.cookiejar


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
        correct_name = ""
        correct_password = ""
        for i in mylist:
            if user_number == i.number:
                is_exist = 1
                correct_name = i.name
                correct_password = i.password

                break
        if is_exist == 0:
            post = "用户不存在"
        else:
            if user_password == "":
                post = "请输入密码"
            else:
                checkcode = hashlib.md5(user_password.encode("utf-8")).hexdigest()
                if checkcode == correct_password:
                    request.session['account']=user_number
                    request.session['username']=correct_name
                    request.session['usertype']=i.types
                    post = "登陆成功"
                    if i.types=="student":
                        return HttpResponseRedirect('/homepage/main.html')
                    if i.types=="judge":
                        return HttpResponseRedirect('/homepage/main_judge.html')
                    if i.types=="team_manager":
                        return HttpResponseRedirect('/homepage/main_team.html')
                    if i.types=="web_manager":
                        return HttpResponseRedirect('/homepage/main_web.html')
                else:
                    post = "密码错误"
    html = template.render(locals())
    return HttpResponse(html)


def homepage(request):
    template = get_template('main.html')
    html = template.render(locals())
    return HttpResponse(html)


def homepage_info(request):
    post = request.session.get('username')
    if request.session.get('usertype')=="student":
        template = get_template('left.html')
    elif request.session.get('usertype')=="judge":
        template = get_template('left_judge.html')
    elif request.session.get('usertype')=="team_manager":
        template = get_template('left_team.html')
    else:
        template = get_template('left_web.html')
    html = template.render(locals())
    return HttpResponse(html)

def homepage_deal(request, url):
    post = request.session.get('username')
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
    template = get_template('index.html')
    html = template.render(locals())
    return HttpResponse(html)

@csrf_exempt
def tsinghua(request):
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
    msg = ""
    query_msg = ""
    type = ""
    if login_result.find('用户名或密码错误') != -1:
        msg = '用户名或密码错误，登录失败'
    elif login_result.find('没有登陆网络学堂的权限') != -1:
        msg = '您没有登陆权限！请确认是清华教工或学生！'
    else:
        cookie = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

        resp = opener.open(my_request)
        url = "http://learn.tsinghua.edu.cn/MultiLanguage/lesson/student/mainstudent.jsp"
        req = urllib.request.Request(url, headers=headers)
        resp = opener.open(req)

        url = "http://learn.tsinghua.edu.cn/MultiLanguage/vspace/vspace_userinfo1.jsp"
        req = urllib.request.Request(url, headers=headers)
        resp = opener.open(req)

        user_info = resp.read().decode('utf-8')

        p = r'tr_l2[^>]+>(.+)</td>'
        pattern = re.compile(p)
        username = pattern.findall(user_info)[0]
        # print(username + '同学，你好')

        p_student = r'tr_l[^>]+>(.+)</td>'
        pattern_student = re.compile(p_student)
        student_number = pattern_student.findall(user_info)[0]
        # print('你的学号：' + student_number)

        p_id = r'id_card[^>]+>(.+)</td>'
        pattern_id = re.compile(p_id)
        id_card = pattern_id.findall(user_info)[0]
        # print('你的身份证号：' + id_card)

        p_folk = r'folk[^>]+>(.+)</td>'
        pattern_folk = re.compile(p_folk)
        folk = pattern_folk.findall(user_info)[0]
        # print('你的民族：' + folk)

        p_zzmm = r'zzmm[^>]+>(.+)</td>'
        pattern_zzmm = re.compile(p_zzmm)
        zzmm = pattern_zzmm.findall(user_info)[0]
        # print('政治面貌：' + zzmm)

        p_email = r'email[^>]+>(.+)</td>'
        pattern_email = re.compile(p_email)
        email = pattern_email.findall(user_info)[0]
        # print('你的邮箱：' + email)
        request.session['account'] = user_name
        request.session['username'] = username
        request.session['student_number'] = student_number
        request.session['id_card'] = id_card
        request.session['folk'] = folk
        request.session['zzmm'] = zzmm
        request.session['email'] = email
        msg = username + '同学，你好！即将跳转至主界面。'
        if not query_student(student_number, username):
            query_msg = "第一次登陆，请稍后修改个人信息！"
            Employee.objects.create(name=username, mail=email, number=student_number)
            type = "student"
        else:
            mylist = Employee.objects.all()
            for i in mylist:
                if student_number == i.number:
                    type = i.types
                    break
        request.session['usertype'] = type
    response = HttpResponse(json.dumps({"msg": msg,
                                        "query_msg": query_msg,
                                        "type": type}))
    return response


def query_student(student_number, username):
    mylist = Employee.objects.all()
    post = "查询结果："
    is_exist = False
    if student_number == "":
        is_exist = False
    else:
        for i in mylist:
            if student_number == i.number and username == i.name:
                is_exist = True
                break
    return is_exist

@csrf_exempt
def checkin(request):
    template = get_template('checkin_index.html')
    html = template.render(locals())
    return HttpResponse(html)
#-------------------------------get model fuction---------------------
def get_people_list():
    mylist = []
    all_people_list = Employee.objects.all()
    for i in all_people_list:
         mylist.append(model_to_dict(i))
    return mylist

def get_team_list():
    mylist = []
    all_team_list = Team.objects.all()
    for i in all_team_list:
         mylist.append(model_to_dict(i))
    return mylist

def get_interview_list():
    mylist = []
    all_interview_list = Interview.objects.all()
    for i in all_interview_list:
         mylist.append(model_to_dict(i))
    for i in mylist:
        list1=i['judge_list'].split("++++")
        i['judge_list']=""
        list3=[]
        for j in list1:
            list2=j.split(" ")
            list3.append(list2[1])
        i['judge_list']=" ".join(list3)
    return mylist

def get_employee(person_number):
    all_people_list = Employee.objects.all()
    for i in all_people_list:
        if(i.number==person_number):
            return i
    

#-------------------------------manage_student.html---------------------


    

@csrf_exempt
def manage_type(request):
    template = get_template('manage_student.html')
    dict = request.POST
    mylist = get_people_list()
    for i in dict:
        if "add" in i:
            Employee.objects.create(number=request.POST['number'],password=request.POST['password'],types='judge')
            mylist = get_people_list()
    html = template.render(locals())
    return HttpResponse(html)

@csrf_exempt
def del_mem(request):
    if request.is_ajax():
        Member_num = request.POST.get('Member_num')
        Employee.objects.filter(number=Member_num).delete()
        info = "已删除成员\"" + str(Member_num) + "\""
        response = HttpResponse(json.dumps({"info": info}))
        return response

@csrf_exempt
def set_student(request):
    if request.is_ajax():
        Member_num = request.POST.get('Member_num')
        
        Type = request.POST.get('set_type')
        # Mem = get_employee(Member_num)
        # Mem.update(number=str(Member_num))
        Mem = Employee.objects.get(number = Member_num)
        Mem.types = Type
        Mem.save()
        print(Mem.types)
        info = "已将成员\"" + str(Member_num) + "\"类型改为"+Type+Mem.number
        response = HttpResponse(json.dumps({"info": info}))
        return response

#-------------------------------manage_team.html---------------------


@csrf_exempt
def manage_team(request):
    template = get_template('manage_team.html')
    dict = request.POST
    mylist = get_team_list()
    for i in dict:
        if "add" in i:
            order = "add"

            Team.objects.create(name=request.POST['team_name'], captain="加油鸭")
            mylist = get_team_list()
    post=request.session.get('username')
    html = template.render(locals())
    return HttpResponse(html)

@csrf_exempt
def del_team(request):
    if request.is_ajax():
        team_name = request.POST.get('team_name')
        Team.objects.filter(name=team_name).first().delete()
        info = "已删除队伍\"" + str(team_name) + "\""
        response = HttpResponse(json.dumps({"info": info}))
        return response

#-------------------------------manage_signup.html---------------------
@csrf_exempt
def sign_up(request):

    template = get_template('manage_signup.html')
    # username=request.session.get('username')
    user_number=request.session.get('account')
    person_model = Employee.objects.get(number = user_number)
    person=[]
    if person_model.choose=="":
        person=[]
    else:
        person = person_model.choose.split("++++")

    msg = ""
    order = ""
    mylist = get_team_list()
    i=0
    while i<len(mylist):
        if mylist[i]['name'] in person:
            mylist.pop(i)
            i=i-1
        i=i+1
    html = template.render(locals())
    return HttpResponse(html)

@csrf_exempt
def del_choose(request):
    if request.is_ajax():
        person_num=request.session.get('account')
        team_name = int(request.POST.get('choose'))
        person = Employee.objects.get(number = person_num)

        
        list1 = person.choose.split("++++")
        list1.pop(team_name)
        person.choose = "++++".join(list1)
        person.save()
        info = person_num+"已删除志愿\"" + str(team_name+1) + "\""
        response = HttpResponse(json.dumps({"info": info}))
        return response

@csrf_exempt
def get_choose(request):
    if request.is_ajax():
        person_num=request.session.get('account')
        team_name = request.POST.get('team_name')
        person = Employee.objects.get(number = person_num)
        if person.choose=="":
            list1=[]
        else:
            list1 = person.choose.split("++++")

        list1.append(team_name)

        person.choose = "++++".join(list1)
        person.save()

        info = person_num+"已设置队伍\"" + str(team_name) + "\"为志愿"
        response = HttpResponse(json.dumps({"info": info}))
        return response

#-------------------------------manage_info.html---------------------
@csrf_exempt
def get_student_info(request):
    if request.is_ajax():
        student_name = request.session.get('username')
        student = Employee.objects.filter(name=student_name).first()
        response = HttpResponse(json.dumps(model_to_dict(student)))
        return response

@csrf_exempt
def modify_info(request):
    if request.is_ajax():
        name = request.POST.get('name')
        number = request.POST.get('number')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        old_pwd = request.POST.get('old_pwd')
        new_pwd = request.POST.get('new_pwd')
        info = "信息修改成功！"
        if name == "":
            info = "姓名不能为空！"
        elif number == "":
            info = "学号不能为空！"
        elif major == "":
            info = "专业不能为空！"
        elif grade == "":
            info = "年级不能为空！"
        elif email == "":
            info = "邮箱不能为空！"
        elif phone == "":
            info = "手机号码不能为空！"
        elif old_pwd == "":
            info = "密码不能为空！"
        elif new_pwd == "":
            info = "新密码不能为空！"
        else:
            phone_pat = re.compile('^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
            res = re.search(phone_pat, phone)
            if not res:
                info = "手机号格式不正确"
            else:
                student = Employee.objects.filter(name=name).first()
                old_pwd2 = student.password
                if old_pwd != old_pwd2:
                    info = old_pwd2
                else:
                    student1 = Employee.objects.filter(name=name)
                    student1.update(name=name,
                                    number=number,
                                    major=major,
                                    grade=grade,
                                    mail=email,
                                    phone_number=phone,
                                    password=new_pwd)
        response = HttpResponse(json.dumps({"info": info}))
        return response

#-------------------------------interview_edit.html---------------------


@csrf_exempt
def interview_edit(request):
    template = get_template('interview_edit.html')
    # dict = request.POST
    temp_list=[]
    people_list = get_people_list()
    judge_list=[]
    for i in people_list:
        if i['types']== 'judge':
            judge_list.append({"number":i["number"],"name":i["name"],"phone_number":i["phone_number"],"mail":i["mail"]})

    # for i in dict:
    #     if "add" in i:
    #         order = "add"

    #         Team.objects.create(name=request.POST['team_name'], captain="加油鸭")
    #         mylist = get_team_list()
    post=request.session.get('username')
    html = template.render(locals())
    return HttpResponse(html)


@csrf_exempt
def set_judge(request):
    if request.is_ajax():
        team_name = request.POST.get('team_name')
        Team.objects.filter(name=team_name).first().delete()
        info = "已删除队伍\"" + str(team_name) + "\""
        response = HttpResponse(json.dumps({"info": info}))
        return response

@csrf_exempt
def new_interview(request):
    if request.is_ajax():
        print(request.body)
        json_data=json.loads(request.body.decode('utf-8'))
        print(json_data)
        print(json_data['team'])
        print(json_data['temp_list'])
        print(type(json_data['temp_list']))
        list1=json_data['temp_list']
        aa=[]
        for i in list1:
            aa.append(i['number']+" "+i['name']+" "+i['phone_number']+" "+i['mail'])
        bb="++++".join(aa)
        Interview.objects.create(team=json_data['team'],
                                date=json_data['date'],
                                location=json_data['location'],
                                start_time=json_data['start_time'],
                                end_time=json_data['end_time'],
                                judge_list=bb,
                                remarks=json_data['remarks'])
        # info = "lalala"
        info = "已建立面试 \"" + str(request.body.decode('utf-8'))
        response = HttpResponse(json.dumps({"info": info}))
        return response

# @csrf_exempt
# def del_team(request):
#     if request.is_ajax():
#         team_name = request.POST.get('team_name')
#         Team.objects.filter(name=team_name).first().delete()
#         info = "已删除队伍\"" + str(team_name) + "\""
#         response = HttpResponse(json.dumps({"info": info}))
#         return response


#-------------------------------manage_interview.html---------------------


@csrf_exempt
def manage_interview(request):
    template = get_template('manage_interview.html')
    interview_list = get_interview_list()
    post=request.session.get('username')
    html = template.render(locals())    
    return HttpResponse(html)


@csrf_exempt
def del_interview(request):
    if request.is_ajax():
        print(request.body)
        temp = json.loads(request.body.decode('utf-8'))
        json_data = temp['list']
        print(json_data)
        print(type(json_data))
        Interview.objects.filter(id=str(json_data['id'])).delete()

        # info = "lalala"
        info = "已删除面试 \"" + str(request.body.decode('utf-8'))
        response = HttpResponse(json.dumps({"info": info}))
        return response

#-------------------------------send_txt.html---------------------

def manage_send_txt(request):
    template = get_template('send_txt.html')
    msg = ""
    order = ""
    dict = request.POST
    mylist = get_people_list()
    # for i in dict:
    #     if "add" in i:
    #         order = "add"
    #         Team.objects.create(name=request.POST['team_name'], captain="暂无")
    #         mylist = get_team_list()
    # post = "order is " + order
    html = template.render(locals())
    return HttpResponse(html)
@csrf_exempt
def send_txt(request):
    if request.is_ajax():
        Member_name = request.POST.get('Member_name')
        txt = request.POST.get('txt')
        Mem = Employee.objects.get(name = Member_name)
        if txt != "":
            if Mem.txted=="":
                list1=[]
            else:
                list1 = Mem.txted.split("++++")
            list1.append(txt)
            if len(list1)>10:
                list1.pop(0)

            Mem.txted = "++++".join(list1)
            Mem.save()
            info = "发送成功"
            gg=0
        else:
            info = "推文内容不能为空"
            gg=1
        #document.getElementById('tui').value="txt"
        response = HttpResponse(json.dumps({"info": info, "gg":gg}))
        return response

#-------------------------------notice.html---------------------
@csrf_exempt
def manage_notice(request):
    template = get_template('notice.html')
    msg = ""
    order = ""
    dict = request.POST
    post=request.session.get('username')
    Mem = Employee.objects.get(name = post)
    if Mem.txted=="":
        mylist=[]
    else:
        mylist = Mem.txted.split("++++")
    # for i in dict:
    #     if "add" in i:
    #         order = "add"
    #         Team.objects.create(name=request.POST['team_name'], captain="暂无")
    #         mylist = get_team_list()
    # post = "order is " + order
    html = template.render(locals())
    return HttpResponse(html)

@csrf_exempt
def notice(request):
    if request.is_ajax():
        hao = int(request.POST.get('idd'))
        post=request.session.get('username')
        Mem = Employee.objects.get(name = post)
        list1 = Mem.txted.split("++++")
        list1.pop(hao)
        print(len(list1))
        Mem.txted = "++++".join(list1)
        Mem.save()
        #document.getElementById('tui').value="txt"
        info=""
        response = HttpResponse(json.dumps({"info": info }))
        return response


#-------------------------------get_qrcode---------------------
@csrf_exempt
def get_qrcode(request):
    if request.is_ajax():
        url = request.POST.get('url')
        path = "static/qrcode/%s.png" % time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))
        path = path.replace(':', '-')
        produce_qrcode(url, path)
        path = "/" + path
        info = "生成成功"
        response = HttpResponse(json.dumps({"info": info,
                                            "path": path}))
        return response
