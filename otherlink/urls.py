from django.urls import re_path
from otherlink.views import OtherlinkProcess
from django.conf import settings
from django.conf.urls.static import static

app_name = 'otheruser_app'

urlpatterns = [
    re_path('', OtherlinkProcess.as_view(), name="otheruser_home"),
    ]

# 설정하고자 하는 url은 GET 방식으로 받는 html route 경로를 따라야함
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)