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
    'ID_EXIST': '이미 존재하는 아이디 입니다.',
    'NO_EXIST_ID' : '존재하지 않는 아이디 입니다.',
    'MISSING_INPUT': '필수항목을 작성해주세요.',
    'PASSWORD_CHECK': '비밀번호를 확인해주세요',
}

def index(request):
    return render(request, 'index.html')

def verified_callback(user):
    user.is_active = True

def business_signup(request):
    context = {
            'error': {
                'state': False,
                'msg': '',
            }
        }

    if request.method == 'POST':
        userid = request.POST['signup-name']
        password = request.POST['signup-password']
        password_check = request.POST['signup-password-check']
        full_name = request.POST['signup-fullname']

        if full_name.find(' '):
            first_name=full_name.split()[0]
            last_name=full_name.split()[1]

        else: 
            first_name=full_name
            last_name='',

        user = User.objects.filter(username=userid)

        if (len(user) != 0):
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['ID_EXIST']
        
        if (not userid or not password or not password_check or not full_name):
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['INPUT_MISSING']

        if (password != password_check):
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['PW_CHECK']

        if (context['error']['state'] is False):
            user = User.objects.create_user(
                username=userid,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            Profile.objects.create(
                user=user,
                name=full_name,
            )

            auth.login(request, user)

            return redirect('index')

    return render(request, 'personal_signup.html', context)



def personal_signup(request):
    context = {
            'error': {
                'state': False,
                'msg': '',
            }
    }

    if request.method == 'POST':
        userid = request.POST['signup-username']
        email = request.POST['signup-email']
        password = request.POST['signup-password']
        password_check = request.POST['signup-password-check']
        full_name = request.POST['signup-fullname']

        if full_name.find(' '):
            first_name=full_name.split()[0]
            last_name=full_name.split()[1]

        else: 
            first_name=full_name
            last_name='',

        user = User.objects.filter(username=userid)

        if (len(user) != 0):
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['ID_EXIST']
        
        if (not userid or not password or not password_check or not full_name):
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['INPUT_MISSING']

        if (password != password_check):
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['PW_CHECK']

        if (context['error']['state'] is False):
            user = User.objects.create_user(
                username=userid,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            PersonalUser.objects.create(
                user=user,
                email=email,
                name=full_name,
            )

            auth.login(request, user)

            return redirect('index')

    return render(request, 'personal_signup.html', context)


def login(request) :
 
    context = {
        'error': {
            'state': False,
            'msg': '',
        }
    }
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        userid = request.POST['login-name']
        password = request.POST['login-password']

        if (not userid or not password):
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['ID_PW_MISSING']
            return render(request, 'login.html', context)

        try: 
            user = User.objects.get(username=userid)
        except:
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['ID_NOT_EXIST']
            return render(request, 'login.html', context)

        auth_user = auth.authenticate(username=userid, password=password)

        if(auth_user):
            auth.login(request, auth_user)
            return redirect('index')

    return render(request, 'index.html')

def logout(request) :
    if request.method == 'POST' :
        auth.logout(request)
        
    return redirect('index')

class BusinessUserDetailView(generic.DeleteView) :
    model = BusinessUser
    template_name = 'BUprofile.html'

    def get(self, request, *args, **kwargs) :
        buser = BusinessUser.objects.all()
        context = {'buser':buser}
        return render(request, 'BUprofile.html', context)

    def post(self, request, *args, **kwargs) :
        return redirect('userinfo:BUprofile', kwargs['pk'])


class CafeListView(generic.ListView) :
    model = StudyCafe
    template_name = 'cafelist.html'
    context_object_name = 'cafelists'

    def post(self, request, *args, **kwargs) :
        return redirect('studycafe:cafelist')


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

        return redirect('studycafe:cafelist')


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

        return redirect('studycafe:cafedetail', kwargs['pk'])