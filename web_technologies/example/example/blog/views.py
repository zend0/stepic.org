# from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from blog.models import Category, Post


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