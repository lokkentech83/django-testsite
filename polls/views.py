from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list" : latest_question_list,
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
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, id=question_id)
    return render(request, "polls/results.html", {"question" : question})

    

def vote(request, question_id) :
    question = get_object_or_404(Question, pk=question_id)

    try :
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist) :
        return render(request, "polls/detail.html", {"question" : question, "error_message" : "You didn't select a choice."})
    else :
        selected_choice.votes += 1
        selected_choice.save()
        # reverse를 이용하여 url하드코딩을 하지않도록 함. 
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,))) # "/polls/3/results/"

    # return HttpResponse("You're voting on question %s." % question_id)


class IndexView(generic.ListView) :
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self) -> QuerySet[Any]:
        # return Question.objects.order_by("-pub_date")[:5]
        # Question.objects.filter (pub_date__lte = timezone.now ())는 timezone.now보다 pub_date가 작거나 같은 Question을 포함하는 queryset을 반환합니다.
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
    
class DetailView(generic.DetailView) :
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self) -> QuerySet[Any]:
        # return super().get_queryset()
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView) :
    model = Question
    template_name = "polls/results.html"