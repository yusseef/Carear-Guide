from django.shortcuts import render, redirect
from .models import SurveyUser
from django.http import HttpResponse
from .forms import SigninForm
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
    qs = SurveyUser.objects.filter(pk=pk)
    context = {'qs':qs}
    return render(request, 'survey.html', context)