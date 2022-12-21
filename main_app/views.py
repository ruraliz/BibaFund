from django.shortcuts import render
from django.http import HttpResponse
#Cat model that is connected to the Dtabase
from .models import Fund, Job, Activity
# add these lines to the imports at the top
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class ActivityCreate( LoginRequiredMixin, CreateView):
  model = Activity
  fields = ['applied', 'remindtoapply']
  success_url = '/activity'
  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user= self.request.user
    self.object.save()
    return HttpResponseRedirect('/activity')


class ActivityUpdate(LoginRequiredMixin, UpdateView):
  model = Activity
  fields = ['applied', 'remindtoapply']
  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    return HttpResponseRedirect('/activity')


class ActivityDelete(LoginRequiredMixin, DeleteView):
  model = Activity
  success_url = '/activity'


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

@login_required
def fund(request):
    funds= list(Fund.objects.all())
    return render(request, 'funds/index.html', { 'funds': funds })

@login_required
def job(request):
    jobs= list(Job.objects.all())
    return render(request, 'jobs/index.html', { 'jobs': jobs })

@login_required
def fund_apply(request, fund_id):
    fund = Fund.objects.get(id=fund_id)
    return render(request, 'funds/apply.html',{'fund': fund})

@login_required
def job_apply(request, job_id):
    job = Job.objects.get(id=job_id)
    return render(request, 'jobs/apply.html',{'job': job})

@login_required
def activity(request):
    activities = list(Activity.objects.all())
    return render(request, 'activity.html',{'activities': activities})
    
@login_required
def profile(request, username):
  user = User.objects.get(username=username)
  funds= Fund.objects.filter(user=user)
  jobs= Job.objects.filter(user=user)
  return render(request, 'profile.html', {'username': username,'funds': funds, 'job': jobs,})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
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