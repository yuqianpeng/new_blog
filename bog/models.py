#coding:utf-8
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=20,help_text='标题')
    context = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User',related_name='topics_of',on_delete=models.CASCADE)

class Comment(models.Model):

    content = models.TextField(max_length=200,help_text='评论')
    created = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey('Blog',related_name='comments_of',on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User',related_name='comments_of',on_delete=models.CASCADE,blank=True,null=True)