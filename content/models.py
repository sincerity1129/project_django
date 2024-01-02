from django.db import models

# Create your models here.
class Contents(models.Model):
    nickname = models.CharField(max_length=30) # 글쓴이 이름
    content_image = models.CharField(max_length=200) # 피드 내 이미지
    content_text = models.TextField() # 피드 내용
    heart_count = models.IntegerField(default=0) # 피드 좋아요 수
    
    class Meta:
        db_table = 'Contents'
        
        
class Comment(models.Model):
    comment_user_nickname = models.CharField(max_length=30) # 글쓴이 계정
    feed_number = models.IntegerField() # 피드 번호
    comment_text = models.TextField() # 댓글 내용
    
    class Meta:
        db_table = 'Comment'   