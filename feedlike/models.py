from django.db import models

# Create your models here.
class Follow(models.Model):
    own_user = models.CharField(max_length=30) # 본인 email
    following = models.CharField(max_length=30) # following 누른 사람 email
    
    class Meta:
        db_table = 'Follow'
        
class FeedLike(models.Model):
    feed_number = models.IntegerField() # 게시판 번호
    like_user_email = models.CharField(max_length=30) # 좋아요 누른 사람 email
    
    class Meta:
        db_table = 'FeedLike'