# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator

from qa.models import Question, Answer


# Create your views here.
@require_GET
def question_list(request):

    questions = Question.objects
    questions = questions.order_by('id')
    questions = questions.reverse()

    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)

    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)  # Page

    print(paginator.page_range)

    return render(request, 'qa/questions_list.html', {
        'question':  page.object_list,
        'paginator': paginator,
        'page':      page,
    })


@require_GET
def pop_question_list(request):

    questions = Question.objects
    questions = questions.order_by('rating')
    questions = questions.reverse()

    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)

    paginator = Paginator(questions, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)  # Page

    print(paginator.page_range)

    return render(request, 'qa/questions_list.html', {
        'question':  page.object_list,
        'paginator': paginator,
        'page':      page,
    })


@require_GET
def question_details(request, slug):
    question = get_object_or_404(Question, id=slug)

    answers = Answer.objects.filter(question=question)
    answers = answers.order_by('id')
    answers = answers.reverse()
    return render(request, 'qa/question_details.html', {
        'question': question,
        'answer': answers,
    })
