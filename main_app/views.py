from django.shortcuts import render
from django.http import HttpResponse
#Cat model that is connected to the Dtabase
from .models import Fund, Job
# add these lines to the imports at the top
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def investment(request):
    return render(request, 'investment.html')

def team(request):
    return render(request, 'team.html')

def fund(request):
    funds= list(Fund.objects.all())
    return render(request, 'funds/index.html', { 'funds': funds })

def job(request):
    jobs= list(Job.objects.all())
    return render(request, 'jobs/index.html', { 'jobs': jobs })

def fund_apply(request, fund_id):
    fund = Fund.objects.get(id=fund_id)
    return render(request, 'funds/apply.html',{'fund': fund})

def job_apply(request, job_id):
    job = Job.objects.get(id=job_id)
    return render(request, 'jobs/apply.html',{'job': job})

def profile(request, username):
  user = User.objects.get(username=username)
  funds= Fund.objects.filter(user=user)
  jobs= Job.objects.filter(user=user)
  return render(request, 'profile.html', {'username': username, 'fund': funds, 'job': jobs})

def login_view(request):
     # if post, then authenticate (user submitted username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled.')
            else:
                print('The username and/or password is incorrect.')
    else: # it was a get request so send the emtpy login form
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form })