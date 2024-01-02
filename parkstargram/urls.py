from django.contrib import admin
from django.urls import path, include
from parkstargram.views import PreviewProcess


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PreviewProcess.as_view(), name='preview_home'),
    path('', include('user.urls')),
    path('otheruser/', include('otherlink.urls')),
    path('content/', include('content.urls')),
    path('follow/', include('feedlike.urls')),
]


