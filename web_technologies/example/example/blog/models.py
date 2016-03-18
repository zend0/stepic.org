from django.db import models


# Create your models here.
class Category(models.Model):

    title = models.CharField(max_length=255)


class Tag(models.Model):

    title = models.CharField(max_length=64)


class PostStatus(models.Model):

    views = models.IntegerField()
    likes = models.IntegerField()


class Post(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    creation_date = models.DateTimeField(blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    status = models.OneToOneField(PostStatus)
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/post/%d/' % self.pk

    class Meta:
        db_table = 'blogposts'
        ordering = ['-creation_date']



