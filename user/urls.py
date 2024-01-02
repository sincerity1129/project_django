from django.urls import path
from user.views import SignUp, SignIn, email_duplicate, nickname_duplicate

app_name = 'user_app'

urlpatterns = [
    path('login', SignIn.as_view(), name="login"),
    path('join', SignUp.as_view(), name="join"),
    path('email_duplicate', email_duplicate, name="email_duplicate"),
    path('nickname_duplicate', nickname_duplicate, name="nickname_duplicate"),
]