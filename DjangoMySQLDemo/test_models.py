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


class PublisherTestCase(TestCase):
    def setUp(self):
        Publisher.objects.create(pub_name="yec", city="Beijing")

    def test_employee(self):
        user = Publisher.objects.get(pub_name="yec")
        self.assertEqual(user.city, "Beijing")


class BookTestCase(TestCase):
    def setUp(self):
        Book.objects.create(book_name="Game", author="yec",
                            pub_date="2018")

    def test_employee(self):
        user = Book.objects.get(author="yec")
        self.assertEqual(user.book_name, "Game")
        self.assertEqual(user.pub_date, "2018")
