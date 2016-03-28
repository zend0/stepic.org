# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET

from qa.models import Question, Answer

# Create your views here.
@require_GET
def question_list(request):
    """
    question = get_object_or_404(Question, slug=slug)
    try:
        vote = post.votes.filter(user=request.user)[0]
    except Vote.DoesNotExist:
        vote = None
    return render(request, 'qa/questions_list.html', {
        'question': question,
    })
    """
    try:
        question = Question.objects.get(pk=3)
    except Question.DoesNotExist:
        question = None

    # print(question.title)
    return HttpResponse(question.title)

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



@require_GET
def question_details(request, slug):
    question = get_object_or_404(Question, slug=slug)
    return render(request, 'qa/questions_list.html', {
        'question': question,
    })


def test(request, *args, **kwargs):
    return HttpResponse('OK')

