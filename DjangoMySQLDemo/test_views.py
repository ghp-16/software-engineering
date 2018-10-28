from django.test import Client, TestCase
from myblog.views import *

class homePageViewTestCase(TestCase):
    def test_homepage(self):
        response = self.client.post('/homepage/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_deal(self):
        response_main = self.client.post('/homepage/main.html')
        self.assertEqual(response_main.status_code, 200)
        response_top = self.client.post('/homepage/top.html')
        self.assertEqual(response_top.status_code, 200)
        response_left = self.client.post('/homepage/left.html')
        self.assertEqual(response_left.status_code, 200)
        response_student = self.client.post('/homepage/student.html')
        self.assertEqual(response_student.status_code, 200)
        response_info = self.client.post('/homepage/student_info.html')
        self.assertEqual(response_info.status_code, 200)
        response_interview = self.client.post('/homepage/student_interview.html')
        self.assertEqual(response_interview.status_code, 200)
        response_sign = self.client.post('/homepage/student_signup.html')
        self.assertEqual(response_sign.status_code, 200)


class resetViewTestCase(TestCase):
    def test_reset(self):
        response_reset = self.client.post('/reset.html')
        self.assertEqual(response_reset.status_code, 200)


class registerViewTestCase(TestCase):
    myType = {"password": 1, "phone": 2}

    def test_username_out_of_range(self):
        data = {'account': "2016011123",
                'name': "abcdefghijklmnopqrstuvwxyz",
                'password': "abcd12345",
                'phone': "13852663598",
                'e-mail': "m15044481234@163.com"}
        response_reset = self.client.post('/register.html', data)
        msg = "用户名过长"
        self.assertIn(msg, response_reset.content.decode('utf-8'))

    def test_invalid_password(self):
        data = {'account': "2016011123",
                'name': "abcd",
                'password': "abcd",
                'phone': "13852663598",
                'e-mail': "m15044481234@163.com"}
        msg = "密码不符合要求"
        type = self.myType['password']
        self.invalid_input_helper(data, msg, type)
        data['password'] = "abcdabcde"
        self.invalid_input_helper(data, msg, type)
        data['password'] = "012345678"
        self.invalid_input_helper(data, msg, type)
        data['password'] = "abcd12345"
        self.invalid_input_helper(data, msg, type)

    def test_invalid_phone_number(self):
        data = {'account': "2016011123",
                'name': "abcd",
                'password': "abcd12345",
                'phone': "1385266359812",
                'e-mail': "m15044481234@163.com"}
        msg = "手机号格式不正确"
        type = self.myType['phone']
        self.invalid_input_helper(data, msg, type)
        data['phone'] = "1565266845"
        self.invalid_input_helper(data, msg, type)
        data['phone'] = "1565266ab48"
        self.invalid_input_helper(data, msg, type)

    def invalid_input_helper(self, data, msg, mytype):
        response_reset = self.client.post('/register.html', data)
        has_digit = False
        has_alpha = False
        if mytype == self.myType['password']:
            if 'password' in data:
                for i in data['password']:
                    if i.isdigit():
                        has_digit = True
                    elif i.isalpha():
                        has_alpha = True
                if has_digit and has_alpha:
                    self.assertNotIn(msg, response_reset.content.decode('utf-8'))
                else:
                    self.assertIn(msg, response_reset.content.decode('utf-8'))
        elif mytype == self.myType['phone']:
            self.assertIn(msg, response_reset.content.decode('utf-8'))


