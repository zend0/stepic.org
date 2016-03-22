from django.conf.urls import patterns, include, url
from blog.views import post_list

"""
urlpatterns = patterns('blog.views',
    url(r'^$', post_list, name='post-list'),
    url(r'^category/(\d+)/$', 'category_view', name='post-list-by-category'),
    url(r'^(?P<pk>\d+)/$', 'post_detail', name='post-detail'),

    url(r'^category/(\d+)/$', 'category_view'),
    url(r'^(?P<pk>\d+)/$', 'post_detail'),
)
"""

urlpatterns = [
    url(r'^post/(?P<slug>\w+)/$', post_details, name='post-details'),
    url(r'^tag/(?P<slug>\w+)/$', tag_details, name='tag-details'),
]
