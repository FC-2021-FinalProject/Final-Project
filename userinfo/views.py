from django.shortcuts import render, redirect
from django.contrib import auth

def login(request) :
    return render(request, 'login.html')

def logout(request) :
    if request.method == 'POST' :
        auth.logout(request)
        
    return redirect('userinfo:login')