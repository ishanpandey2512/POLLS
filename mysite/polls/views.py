from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice


# Create your views here.

def index(request):
    new_question_list = Question.objects.order_by('-pub_date')[:5]

    # #-indicates descending order
    # #join is used for strings
    # output = ",".join(q.question_text for q in new_question_list)
    # return HttpResponse(output)

    context = {
        "new_question_list": new_question_list  #"key- used inside template": values- in views
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # return HttpResponse("you're looking at question with id %s." % question_id)
    # doesnotexist is always a property of attribute of class that does not exist
    # try:
    #     question = Question.objects.get(pk = question_id)
    # except Question.DoesNotExist:
    #     raise Http404("does not exist")
    # return render(request, 'polls/details.html', {'question': question})

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

