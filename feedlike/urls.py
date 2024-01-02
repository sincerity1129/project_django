from django.urls import path
from feedlike.views import like_click, follow_add

app_name = 'feedlike_app'

urlpatterns = [
    path('like_click', like_click, name='like_click'),
    path('follow_add', follow_add, name='follow_add'),
]


