from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
# Django User Custom
class User(AbstractBaseUser):
    '''
        유저 이름 -> 실제 성명
        유저 닉네임 -> 유저 활동명
        유저 프로필 사진 -> 유저 활동 프로필
        유저 이메일 주소 -> 회원가입할 때 사용하는 아이디
    '''
    password = models.CharField(max_length=255, default=True)
    realname = models.CharField(max_length=30, default=True)
    nickname = models.CharField(max_length=30, unique=True, default=True)
    profile_image = models.TextField(default=False)
    email = models.EmailField(unique=True, default=True)
    follow_number = models.IntegerField(default=0)
    
    USERNAME_FIELD = 'nickname'
    
    class Meta:
        db_table = 'User'