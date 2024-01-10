from django.test import TestCase

from common.db_controller import *
from config.test_cfg import *
from config.default_user_create import Tester
from content.models import Contents, Comment
from user.models import User

class ContentTest(TestCase):
    # 기본 설정
    def setUp(self):
        self.feed_update_content = "피드 업데이트"
        self._session_create()
        self._content_data_create()
        self.feed_ori= self._content_data_filter()
    
    # sesstion add
    def _session_create(self, email=Tester['email']):
        session_data = self.client.session
        session_data['email'] = email
        session_data.save()
    
    # content data create
    def _content_data_create(self):
        db_create(Contents, content_image=content_test_image['file'],
                                nickname=content_test_image['new_feed_content_text'],
                                content_text=content_test_image['new_feed_content_text'])
    
    # content data parsing    
    def _content_data_filter(self):
        content = db_filter(Contents, content_text=content_test_image['new_feed_content_text']).first()
        return content
        
        
    # content test start
    def test_feed_create_image(self):
        response = self.client.post('/content', data=content_test_image)
        self.assertEqual(response.status_code, 301)
        
    def test_feed_create_non_image(self):
        response = self.client.post('/content', data=content_test_non_image)
        self.assertEqual(response.status_code, 301)
        
    def test_feed_update(self):
        feed_update = dict(
            update_feed_id= self.feed_ori.id, 
            update_feed_content=self.feed_update_content
            )
        response = self.client.put('/content', data=feed_update, content_type='application/json')
        self.assertEqual(response.status_code, 301)
        
    def test_feed_delete(self):
        delete_feed_id=dict(
            delete_feed_id=self.feed_ori.id
            )
        response = self.client.delete('/content', data=delete_feed_id, content_type='application/json')
        self.assertEqual(response.status_code, 301)
        
        
class CommnetTest(ContentTest):
    # 기본 설정
    def setUp(self):
        super().setUp()
        self.commnet_content = "댓글"
        self.client.post('/join', data=Tester)
        self._comment_data_create()
        self.comment = self._comment_data_filter()
        
    # comment data create
    def _comment_data_create(self):
        db_create(Comment, comment_user_nickname=Tester['email'],
                               feed_number=self.feed_ori.id,comment_text=self.commnet_content)
        
    # comment data parsing
    def _comment_data_filter(self):
        comment =  db_filter(Comment, feed_number=self.feed_ori.id).first()
        return comment
        
        
    # comment test start    
    def test_comment_create(self):
        
        comment_data=dict(
            comment_feed_number=self.feed_ori.id, 
            comment_text=self.commnet_content
            )
        response = self.client.post('/content/comment', data=comment_data)
        self.assertEqual(response.status_code, 200)
        
    def test_comment_delete(self):
        comment_feed_id=dict(
            comment_feed_id = self.comment.id
        )
        response = self.client.delete('/content/comment', data=comment_feed_id, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        
        
class ETCTest(ContentTest):
    # 기본 설정
    def setUp(self):
        super().setUp()
        self._user_create()
        
    def _user_create(self):
        db_create(User, email=Tester['email'], password=Tester['password'],
                               realname=Tester['realname'], nickname=Tester['nickname'])
    
    # ETC test start
    def test_update_image_upload(self):
        up_load=dict(
            class_info = self.feed_ori.id
        )
        response = self.client.post('/content/update_image_upload', data=up_load)
        self.assertEqual(response.status_code, 200)
        
    def test_profile_image_update(self):
        update_profile=dict(
            update_image_file=content_test_image['file'].replace('media/', '')
        )
        response = self.client.post('/content/profile_image_update', data=update_profile)
        self.assertEqual(response.status_code, 200) 
    
    def test_profile_update_non_password(self):
        response = self.client.post('/content/profile_update', data=profile_update_non_password)
        self.assertEqual(response.status_code, 200)
         
    def test_profile_update_add_password(self):
        response = self.client.post('/content/profile_update', data=profile_update_add_password)
        self.assertEqual(response.status_code, 200)
        
        from django.contrib.auth.hashers import check_password
        update_user=db_filter(User, email=Tester["email"]).first()
        self.assertTrue(check_password(profile_update_add_password['profile_update_password'], update_user.password))
        
        
        
class feedLikeTest(ContentTest):
    def setUp(self):
        super().setUp()
        self.client.post('/join', data=Tester)
        self._session_create(email='otherUser')
        self.user = self._user_filter()
        
    def _user_filter(self):
        user = db_filter(User, email=Tester["email"]).first()
        return user
        
    def test_like_click(self):
        feed_number=dict(
            feed_number = self.feed_ori.id
        )
        create_response = self.client.post('/follow/like_click', data=feed_number)
        content_heart_update = db_filter(Contents, id=self.feed_ori.id).first()
        self.assertTrue(content_heart_update.heart_count, 1)
        self.assertEqual(create_response.status_code, 200)
        
        
    def test_follow_add(self):
        user_id = dict(
            user_id=self.user.id
        )
        response = self.client.post('/follow/follow_add', data=user_id)
        user_follow_update = db_filter(User, email=Tester["email"]).first()
        self.assertTrue(user_follow_update.follow_number, 1)
        self.assertEqual(response.status_code, 200)