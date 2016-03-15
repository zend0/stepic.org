from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):

    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='likes_set')


class Answer(models.Model):

    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question,null=True,on_delete=models.SET_NULL)
    author = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)


'''
class User(models.Model):

    name = models.CharField(max_length=255)
'''
