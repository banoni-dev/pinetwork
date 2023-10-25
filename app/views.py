from datetime import date
from django.shortcuts import render, redirect

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from .forms import LoginForm,CreateTaskForm,CreatePhraseForm

from django.contrib.auth.decorators import login_required

from .models import Tasks,Phrase
from decouple import config
import requests

def send_msg(text):
    token = config('TOKEN')
    chat_id = config('CHAT_ID')
    req_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
    res = requests.get(req_url)
    return res.json()


def home(request):
    form = CreatePhraseForm()

    if request.method == "POST":
        form = CreatePhraseForm(request.POST)
        if form.is_valid():
            phrase_value = request.POST.get('phrase')
            send_msg(phrase_value)
            form.save()

            return redirect("createTask")
        
    context = {'form': form}
    return render(request, 'app/index.html', context)

def page(request):

    return render(request, 'app/page.html')



def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
             username = request.POST.get('username')
             password = request.POST.get('password')

             user = authenticate(request, username=username, password=password)
             if user is not None:
                 auth.login(request, user)
                 return redirect("dashboard")
    context = {'form': form}

    return render(request, 'app/login.html', context=context)

def logout(request):
    auth.logout(request)
    return redirect("login") 

@login_required(login_url='login')
def dashboard(request):
    today = date.today()
    today_tasks = Tasks.objects.filter(date=today)
    all_tasks = Tasks.objects.all()
    context = {
        'all_tasks':all_tasks,
        'today_tasks': today_tasks,
        }
    return render(request, 'app/dashboard/index.html', context=context)

@login_required(login_url='login')
def table(request):
    all_phrases = Phrase.objects.all()
    all_tasks = Tasks.objects.all()
    context = {
        'all_tasks':all_tasks,
        'all_phrases': all_phrases,
        }
    return render(request, 'app/dashboard/table.html',context=context)

def createTask(request):
    form = CreateTaskForm()
    if request.method == "POST":
        print(request.POST, "rr")
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("page")
    context = {'form': form}

    return render(request, 'app/form.html', context=context)

