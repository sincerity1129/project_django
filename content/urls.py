from django.urls import path
from content.views import ContentProcess, CommentProcess, update_image_upload, profile_image_update, profile_update, session_add, session_clear
from django.conf import settings
from django.conf.urls.static import static

from config.path_cfg import DefaultProfileImagePath

app_name = 'content_app'

urlpatterns = [
    path('', ContentProcess.as_view(), name="content_home"),
    path('comment', CommentProcess.as_view(), name="comment"),
    path('profile_image_update',profile_image_update, name='profile_image_update'),
    path('profile_update', profile_update, name='profile_update'),
    path('update_image_upload', update_image_upload, name="update_image_upload"),
    path('session_add', session_add, name='session_add'),
    path('session_clear', session_clear, name="session_clear"),
]

# 설정하고자 하는 url은 GET 방식으로 받는 html route 경로를 따라야함
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)