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
           return redirect('user', pk = user.id)
           

   context = {'form': form}
   return render(request, 'index.html', context) 
   

def Survey(request, pk):
    lst = []
    ID = []
    qs = SurveyUser.objects.filter(pk=pk)
    User = SurveyUser.objects.get(pk = pk)
    questions = Questions.objects.all()
    ids = Questions.objects.all().values_list('id', flat = True)
    for i in ids:
        ID.append(i)
    if request.method == 'POST':
        for i in ID:
            answer = request.POST.get(f"{i}")
            lst.append(answer)
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