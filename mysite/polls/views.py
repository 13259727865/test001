from django.shortcuts import render, get_object_or_404, get_list_or_404

# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils.regex_helper import Choice

from .models import User,Address

def index(request):
    return HttpResponse("Hello World!")

def user(request,id):
    response = "user is %s."
    return HttpResponse(response % id)

def results(request, id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % id)

def vote(request,id):
    return HttpResponse("you are voting on %s" % (id+1))

def userlist(request):
    list = User.objects.all()
    output = ', '.join([q.username for q in list])
    return HttpResponse(output)

def userlist2(request):
    list=User.objects.order_by("create_time")[:3]
    print(list)
    context={"list1":list}
    return render(request,"user_list.html",context)

def address(request,id):
    try:
        address = Address.objects.filter(userid_id=id)
        context={"list":address}
    except Address.DoesNotExist:
        raise Http404("未找到！")
    return render(request,"address.html",context)
    # address = get_list_or_404(Address,userid_id=id)
    # for i in address:
    #     return HttpResponse(i.address)
    # return HttpResponse(address)

def vote2(request, user_id):
    question = get_object_or_404(User, pk=user_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        print(123123)
        return render(request, 'polls/user_list.html', {
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