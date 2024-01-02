from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password, make_password
from django.utils.datastructures import MultiValueDictKeyError
from config.path_cfg import BackGroundRandomImageFolder, ProfileImageFolder


from content.models import Contents, Comment
from feedlike.models import FeedLike, Follow
from user.models import User
from status_message.content_status_code import feed, comment, preview, profile, pagemove, logout
from common.common_controller import json_merge
from common.content_controller import ImageController
from common.db_controller import DBController
from common.common_controller import SessionController


# Create your views here.
class ContentProcess(APIView):
    def get(self, request):
        if request.session['email'] == None:
            return redirect('/login')
        user = DBController.db_filter(User, email= request.session['email']).first()
        
        if user == None:
            return redirect('/login')
        
        # 정보 가져와서 content 정보에 맞게 페이지 띄우기 위해 DB 가져오기
        # 왼쪽 피드 관련된 정보
        content = DBController.db_filter(Contents, nickname=user.nickname).order_by('-id') # 피드 정보 가져오기
        feed_number = DBController.db_filter(FeedLike, like_user_email=user.email).values_list('feed_number', flat=True) # 좋아요 버튼 정보 가져오기
        comment = DBController.all_db_search(Comment) # 댓글 정보 가져오기
        
        # 오른쪽 팔로우 관련된 정보
        exclude_user_all = DBController.db_exclude(User, email= request.session['email']) # 본인을 제외한 user 정보 가져와서 오른쪽 팔로우 영역 처리
        follow = DBController.db_filter(Follow, own_user=request.session['email']).values_list('following', flat=True) # 내가 팔로우 한 사람 목록 가져오기
        follower = DBController.db_filter(Follow, following=request.session['email']).count() # 나를 팔로우한 사람 수
        following = len(follow) # 내가 팔로우한 사람 수
        
        # html에 render하기 위한 json 정보 merge
        user_info = json_merge(contents=content, comments = comment, exclude_users=exclude_user_all, 
                               email=request.session['email'], realname=user.realname, nickname=user.nickname, 
                               profile=user.profile_image, feed_number=feed_number, follow=follow, follower=follower, following=following)
        return render(request, 'content/main.html', context=dict(user_info=user_info))

    def post(self, request):
        try:
            file = request.FILES["file"]
            image = ImageController.image_convert(file, BackGroundRandomImageFolder)
            new_feed_content_text = request.data.get('new_feed_content_text')
            nickname = request.data.get('nickname')
            DBController.db_create(Contents, content_image=image, content_text=new_feed_content_text, nickname=nickname)
            return JsonResponse(feed["success"])
        
        except MultiValueDictKeyError as e:
            image = ImageController.feed_default_random_image_select(BackGroundRandomImageFolder)
            new_feed_content_text = request.data.get('new_feed_content_text')
            nickname = request.data.get('nickname')
            DBController.db_create(Contents, content_image=image, content_text=new_feed_content_text, nickname=nickname)
            return JsonResponse(feed["non_image"])
    
    def put(self, request):
        update_feed_id = request.data.get('update_feed_id')
        update_feed_content = request.data.get('update_feed_content')
        
        feed_id = json_merge(id=update_feed_id)
        DBController.db_update(Contents, feed_id, content_text=update_feed_content)
        return JsonResponse(feed["update"])
    
    def delete(self, request):
        delete_feed_id = request.data.get('delete_feed_id')
        del_content_image = DBController.db_filter(Contents, id=delete_feed_id).first().content_image
        ImageController.image_remove(del_content_image, BackGroundRandomImageFolder)
        DBController.db_delete(Contents, id=delete_feed_id)
        return JsonResponse(feed["delete"])


class CommentProcess(APIView):
    def post(self, request):
        comment_feed_number = request.data.get('comment_feed_number')
        comment_text = request.data.get('comment_text')
        
        user = DBController.db_filter(User, email=request.session['email']).first()
        DBController.db_create(Comment, comment_user_nickname=user.nickname, feed_number=comment_feed_number, comment_text=comment_text)
        return JsonResponse(comment["success"])
    
    def delete(self, request):
        comment_feed_id = request.data.get('comment_feed_id')
        DBController.db_delete(Comment, id=comment_feed_id)
        return JsonResponse(comment["delete"])


# 피드 기존 이미지 업로드 모달에 보여지게 하는 함수
def update_image_upload(request):
    if request.method == 'POST':
        image_id = request.POST.get('class_info').split('_')[-1]
        content = DBController.db_filter(Contents, id=image_id).first()
        image_parser = json_merge(image_parser=content.content_image, id=image_id)
        return JsonResponse(image_parser)


# 프로필 이미지에서 미리기보기 클릭 시 왼쪽 프로필 이미지 변경
def profile_image_update(request):
    if request.method == 'POST':
        update_image_file = request.FILES.get('update_image_file')
        if update_image_file==None:
            preview_image= json_merge(preview=preview["fail"], update_image_file_path=update_image_file)
            return JsonResponse(preview_image)
        
        update_image_file_path = ImageController.image_convert(update_image_file, ProfileImageFolder)
        preview_image = json_merge(preview=preview["success"] ,update_image_file_path=update_image_file_path)
        return JsonResponse(preview_image)

# 프로필 내용 변경하기
def profile_update(request):
    if request.method == 'POST':
        user = DBController.db_filter(User, email=request.session['email']).first()
        user_email = json_merge(email=request.session['email'])
        profile_image_update_image_file = request.FILES.get('profile_image_update_image_file')
        password_update_controller = request.POST.get('password_update_controller')
        
        if password_update_controller=="수정하기":
            if profile_image_update_image_file==None:
                profile_update= json_merge(profile=profile["only_profile_image_fail"], profile_image_update_image_file_path="fail")
                return JsonResponse(profile_update)
            else:
                profile_image_update_image_file_path = ImageController.image_convert(profile_image_update_image_file, ProfileImageFolder)
                ImageController.image_remove(user.profile_image, ProfileImageFolder)
                DBController.db_update(User, user_email, profile_image=profile_image_update_image_file_path)
                profile_update= json_merge(profile=profile["only_profile_image_success"], profile_image_update_image_file_path=profile_image_update_image_file_path)
            return JsonResponse(profile_update)
            
        elif password_update_controller=="해제하기":        
            profile_now_password = request.POST.get('profile_now_password')
            # 비밀번호 일치 여부 확인
            if check_password(profile_now_password, user.password):
                # 프로필 파일 변경 여부 확인
                profile_update_password = request.POST.get('profile_update_password')
                if profile_image_update_image_file==None:
                    DBController.db_update(User, user_email, password=make_password(profile_update_password))
                    profile_update= json_merge(profile=profile["only_password_success"], profile_image_update_image_file_path=profile_image_update_image_file)
                    return JsonResponse(profile_update)
                else:
                    profile_image_update_image_file_path = ImageController.image_convert(profile_image_update_image_file, ProfileImageFolder)
                    ImageController.image_remove(user.profile_image, ProfileImageFolder)
                    DBController.db_update(User, user_email, password=make_password(profile_update_password), profile_image=profile_image_update_image_file_path)
                    profile_update= json_merge(profile=profile["password_profile_image_success"], profile_image_update_image_file_path=profile_image_update_image_file_path)
                return JsonResponse(profile_update)
            
            else:
                profile_update= json_merge(profile=profile["only_password_fail"], profile_image_update_image_file_path="fail")
                return JsonResponse(profile_update)

# 다른페이지 열기 위한 세션 추가
def session_add(request):
     if request.method == 'POST':
         other_user_id = request.POST.get('other_user_id')
         print("check: ", other_user_id)
         SessionController.other_user_seesion_in(request, other_user_id)
         return JsonResponse(pagemove["success"])

        
#로그 아웃 시에 세션 종료
def session_clear(request):
    if request.method == 'POST':
        SessionController.user_session_out(request)
        return JsonResponse(logout["clear"])
