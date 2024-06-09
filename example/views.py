# example/views.py
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a home page or dashboard
        else:
            return HttpResponse('Invalid login credentials')
    return render(request, 'example/login.html')

def index(request):
    context = {
        'current_time': datetime.now()
    }
    return render(request, 'example/index.html', context)