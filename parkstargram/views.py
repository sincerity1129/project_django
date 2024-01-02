from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView

from common.common_controller import json_merge
# Create your views here.
class PreviewProcess(APIView):
    def get(self, request):
        return render(request, 'parkstargram/preview.html')
    
    def post(self, request):
        try:
            session_info=json_merge(session_info=request.session['email'])
            return JsonResponse(session_info)
        except:
            request.session['email']=None
            session_info=json_merge(session_info=request.session['email'])
            return JsonResponse(session_info)
        