from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader #to render templates
from django.http import Http404
# Create your views here.

def index(request):
    new_question_list = Question.objects.order_by('-pub_date')[:5]

    # #-indicates descending order
    # #join is used for strings
    # output = ",".join(q.question_text for q in new_question_list)
    # return HttpResponse(output)

    template = loader.get_template('polls/index.html')
    context = {
        "new_question_list": new_question_list  #"key- used inside template": values- in views
    }
    return  HttpResponse(template.render(context, request))

def detail(request, question_id):
    # return HttpResponse("you're looking at question with id %s." % question_id)


def results(request, question_id):
    result = "you're looking at results of question %s"
    return HttpResponse(result % question_id)

def vote(request, question_id):
    return HttpResponse("you're voting on the question %s" % question_id)

