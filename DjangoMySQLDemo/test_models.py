from django.test import TestCase
from myblog.models import *

class EmployeeTestCase(TestCase):
    def setUp(self):
        Employee.objects.create(name="yec", password="abcd12345",
                                phone_number="15044484931",
                                mail="1215468953@qq.com",
                                types="teacher")
        Employee.objects.create(name="yec1", password="abcd12345",
                                phone_number="15044484931",
                                mail="1215468953@qq.com")

    def test_employee(self):
        user = Employee.objects.get(name="yec")
        self.assertEqual(user.password, "abcd12345")
        self.assertEqual(user.phone_number, "15044484931")
        self.assertEqual(user.mail, "1215468953@qq.com")
        self.assertEqual(user.types, "teacher")

        user1 = Employee.objects.get(name="yec1")
        self.assertEqual(user1.types, "student")
