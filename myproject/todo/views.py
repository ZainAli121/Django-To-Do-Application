from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login as auth_login
# from todo.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')

    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'update_task.html', context)

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'task': task}
    return render(request, 'delete_task.html', context)

def signup(request):
    if request.method == 'POST':
        # check if user enters valid crediantials
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        # check if user already exists
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists')
            return redirect('/signup')
        
        # creates new user if user does not exist
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        messages.success(request, 'Account created successfully')

    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        # check if user enters valid crediantials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        # check if user exists
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid crediantials')
            return redirect('/login')
            
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect('/login')