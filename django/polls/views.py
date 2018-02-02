from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

    # render함수가 내부적으로 처리되는 과정
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, template))


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(id=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    # 위 try문을 한 줄로 표현한 구문
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = "You're looking at results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
