from django.http import JsonResponse

from common.common_controller import json_merge
from common.db_controller import DBController
from user.models import User
from content.models import Contents
from feedlike.models import Follow, FeedLike
from django.db.models import F

from status_message.follow_status_code import feed_like, follow


def like_click(request):
    if request.method == 'POST':
        feed_number = request.POST.get('feed_number').split('_')[-1]
        id_query = json_merge(id=feed_number)
        
        if DBController.db_filter(FeedLike, feed_number=feed_number, like_user_email=request.session['email']).exists():
            DBController.db_delete(FeedLike, feed_number=feed_number)            
            DBController.db_update(Contents, id_query, heart_count=F('heart_count')-1)
            return JsonResponse(feed_like["cancle"])
        else:
            DBController.db_create(FeedLike, feed_number=feed_number, like_user_email=request.session['email'])
            DBController.db_update(Contents, id_query, heart_count=F('heart_count')+1)
            return JsonResponse(feed_like["like"])
        
def follow_add(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id').split('_')[-1]
        following_user = DBController.db_filter(User, id=user_id).first()
        email_query = json_merge(email=following_user.email)

        if DBController.db_filter(Follow, own_user=request.session['email'], following=following_user.email).exists():
            DBController.db_delete(Follow, own_user=request.session['email'], following=following_user.email)
            DBController.db_update(User, email_query, follow_number=F('follow_number')-1)
            follow_info=json_merge(follow=follow["cancle"], nickname=following_user.nickname)
            return JsonResponse(follow_info)
        
        else:
            DBController.db_create(Follow, own_user=request.session['email'], following=following_user.email)
            DBController.db_update(User, email_query, follow_number=F('follow_number')+1)
            follow_info=json_merge(follow=follow["following"], nickname=following_user.nickname)
            return JsonResponse(follow_info)