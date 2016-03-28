from django.shortcuts import render, get_object_or_404
# from django.shortcuts import render
# from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.http import require_GET

from blog.models import Category, Post

from django.core.paginator import Paginator


# Create your views here.
def post_list(request, *args, **kwargs):
    # вывести все посты
    # c = Category(title="Perl")
    # c.save()

    c = Category.objects.create(title="PHP")
    c.title = "About PHP"
    c.save()
    return HttpResponse('OK')

def post_text(request):
    try:
        id = request.GET.get('id')
        obj = Post.objects.get(pk=id)
    except Post.DoesNotExist:
        raise Http404

    return HttpResponse(obj.text, content_type='text/plain')

def home(request):
    # вывести страницу поста
    return HttpResponse('Home page: Mama I coming Home')

def category_view(request, pk=None):
    # вывести все посты
    pass

def post_details(request, pk):
    # вывести страницу поста
    pass

def category_view(request, *args, **kwargs):
    pk=args[0]
    pk=kwargs['pk']

"""
def post_details(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'blog/post_details.html', {
        'post':post,
    })
"""


# короткая альтернатива предыдущей реализации функции
@require_GET
def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_details.html', {
        'post': post,
    })


# Связанные сущности
"""
def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    try:
        vote = post.votes.filter(user=request.user)[0]
    except Vote.DoesNotExist:
        vote = None
    return render(request, 'blog/post_details.html', {
        'post': post,
        'category': post.category,
        'tags': post.tags.all()[:],
        'vote': vote,
    })
"""


# Постраничное отображение
def post_list_all(request):
    posts = Post.objects.filter(is_published=True)
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, limit)
    paginator.baseurl = '/blog/all_posts/?page='
    page = paginator.page(page) # Page
    return render(request, 'blog/post_by_tag.html', {
        'posts': page.object_list,
        'paginator': paginator,
        'page': page,
    })

'''
return render_to_response('blog/post_details.html',{
    'post':post,
    'comments':comments,
})

return render(request,'blog/post_details.html',{
    'post':post,
    'comments':comments,
})
'''