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

    def get(self, request, *args, **kwargs) :
        buser = BusinessUser.objects.all()
        context = {'buser':buser}
        return render(request, 'BUprofile.html', context)

    def post(self, request, *args, **kwargs) :
        return redirect('userinfo:BUprofile', kwargs['pk'])