from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=20,default="你好鸭")
    password = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11,default="18800137836")
    mail = models.CharField(max_length=320,default="example@163.com")
    types = models.CharField(max_length=15, default="student")
    number = models.CharField(max_length=10, default="2016011123")
    major = models.CharField(max_length=15, default="计算机系")
    grade = models.CharField(max_length=5, default="大一")