from django.db import models
from myblog.fields import ListField

class Employee(models.Model):
    name = models.CharField(max_length=20,default="你好鸭")
    password = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11,default="18800137836")
    mail = models.CharField(max_length=320,default="example@163.com")
    types = models.CharField(max_length=15, default="student")
    number = models.CharField(max_length=10, default="2016011123")
    major = models.CharField(max_length=15, default="计算机系")
    grade = models.CharField(max_length=5, default="大一")
    choose = ListField()
    def __str__(self):
        return "%s " % self.choose

class Team(models.Model):
    name = models.CharField(max_length=10 , default="划水队")
    captain = models.CharField(max_length=10 , default="可达鸭")
    captain_num = models.CharField(max_length=10 , default="2016011392")
    # interview = ListField()

class Interview(models.Model):
    team = models.CharField(max_length=32 , default="国标队")
    date = models.CharField(max_length=32 , default="10/30/2018")
    start_time = models.CharField(max_length=32 , default="9:25:00 AM")
    end_time = models.CharField(max_length=32 , default="11:25:00 AM")
    location = models.CharField(max_length=32 , default="蒙民伟楼") 
    remarks = models.CharField(max_length=600 , default="多喝热水") 
    judge_list = ListField()
    def __str__(self):
        return "%s " % self.judge_list
