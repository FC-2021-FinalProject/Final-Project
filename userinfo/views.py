from django.views import generic
from django.shortcuts import render, redirect
from django.contrib import auth

from .models import BusinessUser


def login(request) :
    return render(request, 'login.html')

def logout(request) :
    if request.method == 'POST' :
        auth.logout(request)
        
    return redirect('userinfo:login')

class BusinessUserDetailView(generic.DeleteView) :
    model = BusinessUser
    template_name = 'BUprofile.html'
    context_object_name = 'buser'

    def get(self, request, *args, **kwargs) :
        return render(request, 'BUprofile.html')

    def post(self, request, *args, **kwargs) :
        return redirect('userinfo:BUprofile', kwargs['pk'])