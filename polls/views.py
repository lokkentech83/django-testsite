from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_quest_list" : latest_question_list,
    }
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse("Hello, world. You're at the polls index.")

    # 자주쓰이는 기능은 shortcuts에 단축으로 들어가있으므로 사용하면 편리
    # return HttpResponse(template.render(context,request))
    return render(request, 'polls/index.html', context)



def detail(request, question_id) :
    # try/catch를 이용할경우
    # try :
    #     question = Question.objects.get(pk = question_id)
    # except Question.DoesNotExist :
    #     raise Http404("Question does not exist")
    
    # shortcut을 이용할경우
    question = get_object_or_404(Question, pk=question_id)

    # return HttpResponse("You're looking at question %s." % question_id)
    return render(request, 'polls/detail.html', {"question" : question})

def results(request, question_id) :
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id) :
    return HttpResponse("You're voting on question %s." % question_id)

