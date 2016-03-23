# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET

# Create your views here.


@require_GET
def question_details(request, slug):
    question = get_object_or_404(Question, slug=slug)
    return render(request, 'qa/questions_list.html', {
        'question': question,
    })


def test(request, *args, **kwargs):
    return HttpResponse('OK')

