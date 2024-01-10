from django.test import TestCase
from django.contrib.auth.hashers import check_password

from common.db_controller import *
from config.default_user_create import Tester
from user.models import User

class UserTest(TestCase):
    def test_join(self):
        response = self.client.post('/join', data=Tester)
        self.assertEqual(response.status_code, 200)
        
        user = a.db_filter(User, email=Tester["email"]).first()
        self.assertEqual(user.email, Tester["email"])
        self.assertTrue(check_password(Tester["password"], user.password))
        self.assertEqual(user.realname, Tester["realname"])
        self.assertEqual(user.nickname, Tester["nickname"])
        
    def test_login(self):
        self.client.post('/join', data=Tester)
        response = self.client.post('/login', data=dict(
             email = Tester['email'],
             password = Tester['password']
        ))
        self.assertEqual(response.status_code, 200) 