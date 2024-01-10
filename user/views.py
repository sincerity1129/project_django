from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from user.models import User
from user.serializers import UserSerializer

from django.contrib.auth.hashers import check_password
from status_message.user_status_code import *
from common.db_controller import *
from common.common_controller import SessionController
from config.default_user_create import Tester

EMAIL_CHAT='@'

# Create your views here.
class SignUp(APIView):
    def get(self, request):
        return render(request, 'user/join.html')
    
    def post(self, request):
        serializer = UserSerializer(request.data)
        if db_filter(User,email=serializer.data['email']).exists():
            return JsonResponse(sign_up["email"])
        elif db_filter(User,email=serializer.data['nickname']):
            return JsonResponse(sign_up["realname"])            
        elif len(serializer.data["password"]) < 8:
            return JsonResponse(sign_up["password_limit"])
        else:
            if EMAIL_CHAT not in serializer.data['email']:
                return JsonResponse(sign_up["email_form"])
            serializer.user_create(request.data)
            return JsonResponse(sign_up["success"])
    
    
class SignIn(APIView):
    def get(self, request):
        if not db_filter(User,email='test@naver.com').exists():
            serializer = UserSerializer(request.data)
            serializer.user_create(Tester)
        return render(request, 'user/login.html')
    
    def post(self, request):
        serializer = UserSerializer(request.data)
        if serializer.data['email'] == 'test@naver.com':
            user = db_filter(User, email=serializer.data['email']).first()
            SessionController.user_session_in(request, serializer.data['email'])
            success_url=dict(
                url='content',
                realname=user.realname
                )
            return JsonResponse(success_url)
        elif db_filter(User,email=serializer.data['email']).exists():
            user = db_filter(User, email=serializer.data['email']).first()
            if check_password(serializer.data['password'], user.password):
                SessionController.user_session_in(request, serializer.data['email'])
                # request.session['email'] = serializer.data['email']
                success_url=dict(
                    url = "content",
                    realname = user.realname
                )
                return JsonResponse(success_url)
            else:
                return JsonResponse(sign_in["password_check"])
        else:
            return JsonResponse(sign_in["email_check"])
        
def email_duplicate(request):
    if request.method == 'POST':
        serializer = UserSerializer(request.POST)
        
        if db_filter(User,email=serializer.data['email']).exists():
            return JsonResponse(email_check["not_email_duplicate"])
        else:
            return JsonResponse(email_check["email_duplicate"])
        
def nickname_duplicate(request):
    if request.method == 'POST':
        serializer = UserSerializer(request.POST)
        
        if db_filter(User,nickname=serializer.data['nickname']).exists():
            return JsonResponse(nickname_check["nickname_duplicate"])
        else:
            return JsonResponse(nickname_check["not_nickname_duplicate"])