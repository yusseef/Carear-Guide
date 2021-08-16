from django.shortcuts import render, redirect
from .models import SurveyUser, Questions, SurveyResults
from django.http import HttpResponse
from .forms import SigninForm
from collections import Counter
# Create your views here.
def Signin(request):
   form = SigninForm()
   if request.method == 'POST':
       form = SigninForm(request.POST)

       if form.is_valid():
           user = form.save()
           return redirect('user', pk=user.id)
           

   context = {'form': form}
   return render(request, 'index.html', context) 
   

def Survey(request,pk):
    lst = []
    qs = SurveyUser.objects.filter(pk=pk)
    User = SurveyUser.objects.get(pk = pk)
    questions = Questions.objects.all()
    if request.method == 'POST':
        answer1 = request.POST.get("2")
        answer2 = request.POST.get("3")
        answer3 = request.POST.get("4")
        answer4 = request.POST.get("5")
        print('hi')
        lst.append(answer1)
        lst.append(answer2)
        lst.append(answer3)
        lst.append(answer4)
        List = [x for x in lst if not x=='no']
        counter = Counter(List)
        result = counter.most_common(1)[0][0]
        Final_result = SurveyResults(survey_user= User)
        Final_result.result = result
        Final_result.save()
        return redirect('Result', pk = Final_result.id)
    
    context = {'qs':qs, 'questions':questions}
    return render(request, 'survey.html', context)


def Result(request, pk):
    qs = SurveyResults.objects.get(pk = pk)
    context = {'result': qs}
    return render(request, 'result.html',  context)