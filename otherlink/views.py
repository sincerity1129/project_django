from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.views import APIView
import json 

from content.models import Contents, Comment
from feedlike.models import FeedLike, Follow
from user.models import User
from common.common_controller import json_merge
from common.db_controller import DBController


# Create your views here.
class OtherlinkProcess(APIView):
    def get(self, request):
        user_id =  request.session['id']
        user = DBController.db_filter(User, id= user_id).first()
        session_user = DBController.db_filter(User, email= request.session['email']).first()
        if user == None:
            return redirect('/login')
        
        # 정보 가져와서 content 정보에 맞게 페이지 띄우기 위해 DB 가져오기
        # 왼쪽 피드 관련된 정보
        content = DBController.db_filter(Contents, nickname=user.nickname).order_by('-id') # 피드 정보 가져오기
        feed_number = DBController.all_db_search(FeedLike).values_list('feed_number', flat=True) # 좋아요 버튼 정보 가져오기
        comment = DBController.all_db_search(Comment) # 댓글 정보 가져오기
        
        # 오른쪽 팔로우 관련된 정보
        exclude_user_all = DBController.db_exclude(User, email= request.session['email']) # 본인을 제외한 user 정보 가져와서 오른쪽 팔로우 영역 처리
        follow = DBController.db_filter(Follow, own_user=request.session['email']).values_list('following', flat=True) # 내가 팔로우 한 사람 목록 가져오기
        follower = DBController.db_filter(Follow, following=request.session['email']).count() # 나를 팔로우한 사람 수
        following = len(follow) # 내가 팔로우한 사람 수
        
        
        # html에 render하기 위한 json 정보 merge
        user_info = json_merge(contents=content, comments = comment, exclude_users=exclude_user_all, 
                               email=request.session['email'], realname=user.realname, nickname=user.nickname, 
                               profile=user.profile_image, feed_number=feed_number, follow=follow, follower=follower,
                               following=following, session_user=session_user)

        return render(request, 'otherlink/submain.html', context=dict(user_info=user_info))