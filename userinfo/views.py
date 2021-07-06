from django.views import generic
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import PersonalUser, BusinessUser

def verified_callback(user):
    user.is_active = True


def business_signup(reuest):
    context = {'error': {'state': False, 'msg': ERROR_MSG}}    
    if request.method == 'POST': 
        name = request.POST['signup-name']
        password = request.POST['signup-password']
        email = request.POST['signup-email']

        user = User.objects.create_user(username=name, password=password, email=email)
        BusinessUser.objects.create(user=user,name=name)
        
        user = auth.get_user_model().objects.create(username=name, password=password, email=email)
        # change is_active to True for testing purposes
        user.is_active = True
        # do not send email while testing

        # send_email(user, custom_salt=my_custom_key_salt)
        
        # email_subject = 'Activate Your Account'
        # email_body = ''

        # email = EmailMessage(
        #     email_subject,
        #     email_body,
        #     'from@example.com',
        #     [email],
        #     )
        # email.send(fail_silently=False)
        auth.login(request, user)

        return redirect ('index')

    else:
        return render(request, 'signup.html', context)


def personal_signup(request):
    context = {'error': {'state': False, 'msg': ERROR_MSG}}    
    if request.method == 'POST': 
        name = request.POST['signup-name']
        password = request.POST['signup-password']
        email = request.POST['signup-email']

        user = User.objects.create_user(username=name, password=password, email=email)
        PersonalUser.objects.create(user=user,name=name)
        
        user = auth.get_user_model().objects.create(username=name, password=password, email=email)
        # change is_active to True for testing purposes
        user.is_active = True
        # do not send email while testing
        
        # send_email(user, custom_salt=my_custom_key_salt)
        # email_subject = 'Activate Your Account'
        # email_body = ''

        # email = EmailMessage(
        #     email_subject,
        #     email_body,
        #     'from@example.com',
        #     [email],
        #     )
        # email.send(fail_silently=False)
        auth.login(request, user)

        return redirect ('index')

    else:
        return render(request, 'signup.html', context)



def login(request) :
    context = {'error': {'state': False, 'msg': ERROR_MSG}}

    name = request.POST['login-name']
    password = request.POST['login-password']
    user = auth.authenticate(request, username = name, password = password)
    
    if user is not None:
        auth.login(request, user)
        return redirect('login')
    
    else:
        context['error']['state'] = True
        context['error']['msg'] = ERROR_MSG['MISSING_INPUT']
        return render(request, 'login.html', context)
    
    
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