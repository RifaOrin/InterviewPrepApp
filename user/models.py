from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
 
class Tag(models.Model):
    tag_name = models.CharField(max_length=256)
 
 
class Post(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    bump = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    '''tag = models.ManyToManyField(
        Tag, related_name = 'post', blank=True
    )'''

 
 
class Comments(models.Model):
    text = models.CharField(max_length=256)
    bump = models.IntegerField()
    time = models.DateTimeField(default=timezone.now)
    '''author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )'''
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        Post, on_delete=models.CASCADE
    )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    name = models.CharField(max_length=256, default="<anon>")
    works_at = models.CharField(max_length=256)


    
