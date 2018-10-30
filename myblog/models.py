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

# class Interview(models.Model)
#     team_name = models.CharField(max_length=10 , default="划水队")
#     judge_list = ListField()
    