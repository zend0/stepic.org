from django.db import models

# Create your models here.


class Question(models.Model):

    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(Author,null=True,on_delete=models.SET_NULL)
    likes = models.ManyToManyField(Like)


class Answer(models.Model):

    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    question = models.ForeignKey(Question,null=True,on_delete=models.SET_NULL)
    author = models.ForeignKey(Author,null=True,on_delete=models.SET_NULL)


class Author(models.Model):

    name = models.CharField(max_length=255)
