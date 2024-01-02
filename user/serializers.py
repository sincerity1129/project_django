from rest_framework import serializers
from user.models import User
from django.contrib.auth.hashers import make_password

from config.path_cfg import DefaultProfileImagePath

class UserSerializer(serializers.ModelSerializer):
    def user_create(self, user_info):
        user_data = user_info.copy()
        user_data = {key: str(value) for key, value in user_data.items()}
        user_data['password'] = make_password(user_data['password'])
        # profile_image default 설정 = 흰색
        user_data['profile_image'] = DefaultProfileImagePath
        user = User.objects.create(**dict(user_data))
        return user
    
    class Meta:
        model = User
        fields = ['id', 'password', 'realname', 'nickname', 'profile_image', 'email']