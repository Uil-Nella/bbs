#coding=utf-8

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#论坛实体
class BBS(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256,blank=True,null=True)
    content = models.TextField()
    author = models.ForeignKey('BBS_user')
    view_count = models.IntegerField()
    ranking = models.IntegerField()
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
    
    def __unicode__(self):
        return self.title
    
#class Comment(models.Model):
    
#分类实体
class Category(models.Model):
    name = models.CharField(max_length=32,unique=True)
    administrator = models.ForeignKey('BBS_user')
    
#用户实体
class BBS_user(models.Model):
    user = models.OneToOneField(User)
    signature = models.CharField(max_length=128,default='This guy too lazy to levave anything here')
    photo = models.ImageField(upload_to="upload_imgs/",default="upload_imgs/user-1.jpg")
    
    def __unicode__(self):
        return self.user.username

class test(models.Model):
    test_field = models.CharField(max_length=32) 
    
    
    