from django.contrib import auth
from django.contrib.auth.models import User
from django.http import request
from django.views import generic, View
from django.shortcuts import get_object_or_404, render, redirect

import boto3
from boto3.session import Session
from config.settings import AWS_ACCESS_KEY_ID, AWS_S3_REGION_NAME, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME
from datetime import date, datetime

from .models import PersonalUser, BusinessUser
from studycafe.models import StudyCafe

ERROR_MSG = {
    'EXIST_ID': '이미 존재하는 아이디 입니다.',
    'NO_EXIST_ID' : '존재하지 않는 아이디 입니다.',
    'MISSING_INPUT': '필수항목을 작성해주세요.',
    'PASSWORD_CHECK': '비밀번호를 확인해주세요',
}

def index(request):
    return render(request, 'index.html')

def verified_callback(user):
    user.is_active = True

def business_signup(request):
    if request.method == 'POST': 
        name = request.POST['signup_name']
        password = request.POST['signup_password']
        email = request.POST['signup_email']

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
        return render(request, 'signup.html')


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
        
    return redirect('login')


class BusinessUserDetailView(generic.DeleteView) :
    model = BusinessUser
    template_name = 'BUprofile.html'

    def get(self, request, *args, **kwargs) :
        buser = BusinessUser.objects.all()
        context = {'buser':buser}
        return render(request, 'BUprofile.html', context)

    def post(self, request, *args, **kwargs) :
        return redirect('BUprofile', kwargs['pk'])


class CafeListView(generic.ListView) :
    model = StudyCafe
    template_name = 'cafelist.html'
    context_object_name = 'cafelists'

    def post(self, request, *args, **kwargs) :
        return redirect('cafelist')


class CafeUploadView(View) :
    def get(self, request, *args, **kwargs) :
        return render(request, 'cafeupload.html')

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('image')
        session = Session(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_S3_REGION_NAME,
        )
        s3 = session.resource('s3')
        now = datetime.now().strftime('%Y%H%M%S')
        img_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
            Key=now+file.name,
            Body=file
        )
        s3_url = 'https://django-s3-cj.s3.ap-northeast-2.amazonaws.com/'
        StudyCafe.objects.create(
            name=request.POST['name'],
            address= request.POST.get('address'),
            img = s3_url+now+file.name,
            price_per_hour = request.POST['price_per_hour'],
            business_hour_start = request.POST['business_hour_start'],
            business_hour_end = request.POST['business_hour_end'],
        )

        return redirect('cafelist')


class CafeDetailView(generic.DetailView) :
    model = StudyCafe
    template_name = 'cafedetail.html'
    context_object_name = 'cafe'

    def post(self, request, *args, **kwargs) :
        return render(request, 'cafedetail.html', kwargs['pk'])


class CafeEditView(generic.View) :
    model = StudyCafe
    template_name = 'cafeedit.html'

    def get(self, request, *args, **kwargs) :
        context = {'cafe':get_object_or_404(StudyCafe, pk=kwargs['pk'])}
        return render(request, 'cafeedit.html', context)

    def post(self, request, *args, **kwargs) :
        file = request.FILES.get('image')
        session = Session(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_S3_REGION_NAME,
        )
        s3 = session.resource('s3')
        now = datetime.now().strftime('%Y%H%M%S')
        # img_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
        #     Key=now+file.name,
        #     Body=file
        # )
        s3_url = 'https://django-s3-cj.s3.ap-northeast-2.amazonaws.com/'

        StudyCafe.objects.filter(pk=kwargs['pk']).update(
            name=request.POST['name'],
            address= request.POST.get('address'),
            # img = s3_url+now+file.name,
            price_per_hour = request.POST['price_per_hour'],
            business_hour_start = request.POST['business_hour_start'],
            business_hour_end = request.POST['business_hour_end'],
        )

        return redirect('cafedetail', kwargs['pk'])

def cafedelete(request, cafe_pk) :
    cafe = StudyCafe.objects.filter(pk=cafe_pk)
    cafe.update(is_deleted=True)

    return redirect('BUprofile', cafe_pk)