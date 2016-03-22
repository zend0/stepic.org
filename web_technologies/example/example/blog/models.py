from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Category(models.Model):

    title = models.CharField(max_length=255)


class Tag(models.Model):

    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=64)

    def get_url(self):
        return reverse('blog:tag-details',
                       kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.title


class Status(models.Model):

    views = models.IntegerField()
    likes = models.IntegerField()


class Post(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    creation_date = models.DateTimeField(blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    status = models.OneToOneField(Status)
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/post/%d/' % self.pk

    class Meta:
        # Если хотим задать конкретное имя таблицы
        # db_table = 'blogposts'
        ordering = ['-creation_date']
