from django.contrib import auth
from django.contrib.auth.models import User
from django.http import request
from django.views import generic, View
from django.shortcuts import get_object_or_404, render, redirect

import boto3
from boto3.session import Session
from config.settings import AWS_ACCESS_KEY_ID, AWS_S3_REGION_NAME, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME
from datetime import date, datetime, timedelta,time

from studycafe.models import  PersonalUser, BusinessUser, StudyCafe, Date, HourTime, Seats,  Reservations, Review

ERROR_MSG = {
    'ID_EXIST': '이미 존재하는 아이디 입니다.',
    'NO_EXIST_ID' : '존재하지 않는 아이디 입니다.',
    'MISSING_INPUT': '필수항목을 작성해주세요.',
    'PASSWORD_CHECK': '비밀번호를 확인해주세요',
}

def index(request):
    return render(request, 'index.html')

# function for email authentication
def verified_callback(user):
    user.is_active = True

def business_signup(request):
    validation_context  = {'error': {'state': False,'msg': '',}}

    if request.method == 'POST':
        user_name = request.POST['signup-name']
        user_username=request.POST['signup-username']
        user_email = request.POST['signup-email']
        user_password = request.POST['signup-password']
        password_check = request.POST['signup-password-check']
        registration_number = request.POST['signup-registration-number']

        if len(User.objects.filter(username=user_username)) != 0:
            validation_context['error']['state'] = True
            validation_context['error']['msg'] = ERROR_MSG['ID_EXIST']
        
        if (not user_name or not user_email or not user_password or not password_check or not user_username):
            validation_context['error']['state'] = True
            validation_context['error']['msg'] = ERROR_MSG['MISSING_INPUT']

        if (user_password != password_check):
            validation_context['error']['state'] = True
            validation_context['error']['msg'] = ERROR_MSG['PASSWORD_CHECK']

        if (validation_context['error']['state'] is False):
            user = User.objects.create_user(
                username=user_username,
                email=user_email,
                password=user_password,
            )
            new_account = BusinessUser.objects.create(
                user=user,
                email=user_email,
                name=user_name,
                registration_number=registration_number,
                email_authenticated=True,
            )
 
            auth.login(request, user)
            return redirect('index')
    return render(request, 'business_signup.html', validation_context)


def personal_signup(request):

    validation_context  = {'error': {'state': False,'msg': '',}}

    if request.method == 'POST':

        user_name = request.POST['signup-name']
        user_username=request.POST['signup-username']
        user_email = request.POST['signup-email']
        user_password = request.POST['signup-password']
        password_check = request.POST['signup-password-check']

        if len(User.objects.filter(username=user_name)) != 0:
            validation_context['error']['state'] = True
            validation_context['error']['msg'] = ERROR_MSG['ID_EXIST']
        
        if (not user_name or not user_email or not user_password or not password_check or not user_username):
            validation_context['error']['state'] = True
            validation_context['error']['msg'] = ERROR_MSG['MISSING_INPUT']

        if (user_password != password_check):
            validation_context['error']['state'] = True
            validation_context['error']['msg'] = ERROR_MSG['PASSWORD_CHECK']

        if (validation_context['error']['state'] is False):
            user = User.objects.create_user(
                username=user_username,
                email=user_email,
                password=user_password,
            )
            new_account = PersonalUser.objects.create(
                user=user,
                email=user_email,
                name=user_name,
                email_authenticated=True,
            )
 
            auth.login(request, user)
            return redirect('index')

    return render(request, 'personal_signup.html', validation_context)

def login(request) :

    validation_context = {'error': {'state': False,'msg': '',}}

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        user_name = request.POST['login-name']
        user_password = request.POST['login-password']

        if (not user_name or not user_password):
            validation_context['error']['state'] = True
            validation_context['error']['msg'] = ERROR_MSG['MISSING_INPUT']
            return render(request, 'index.html', validation_context)
        try: 
            user = User.objects.get(username=user_name)
        except:
            validation_context['error']['state'] = True
            validation_context['error']['msg'] = ERROR_MSG['NO_EXIST_ID']
            return render(request, 'index.html', validation_context)

        auth_user = auth.authenticate(username=user_name, password=user_password)

        if (auth_user):
            auth.login(request, auth_user)
            return redirect('index')
    return render(request, 'login.html', validation_context)

def logout(request) :
    if request.method == 'POST' :
        auth.logout(request)
    return redirect('index')

class PersonalUserDetailView(generic.DeleteView) :
    model = PersonalUser
    template_name = 'PUprofile.html'

    def get(self, request, *args, **kwargs) :
        puser = PersonalUser.objects.get(user=request.user)
        context = {'puser': puser}
        return render(request, 'PUprofile.html', context)

    def post(self, request, *args, **kwargs) :
        return redirect('PUprofile', kwargs['pk'])

class BusinessUserDetailView(generic.DeleteView) :
    model = BusinessUser
    template_name = 'BUprofile.html'

    def get(self, request, *args, **kwargs) :
        buser = BusinessUser.objects.get(user=request.user)
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
        businessuser = BusinessUser.objects.get(user=request.user)
        StudyCafe.objects.create(
            name=request.POST['name'],
            businessuser = businessuser,
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

    def get(self, request, *args, **kwargs) :
        cafe = get_object_or_404(StudyCafe, pk=kwargs['pk'])
        reviews = Review.objects.filter(studycafe=cafe)

        context = {'cafe':cafe, 'reviews':reviews}

        return render(request, 'cafedetail.html', context)

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


class ReservationView(generic.View) :
    model = Reservations
    template_name = 'cafedetail.html'
    context_object_name = 'reserv'

    def post(self, request, *args, **kwargs) :
        date = request.POST['date']
        start_time = request.POST['start_time']
        use_time = request.POST['time']
        seat = request.POST['seat']
        studycafe = StudyCafe.objects.get(pk=kwargs['pk'])
        end_time = time(int(int(start_time) + int(use_time)))
        


        if len(Seats.objects.filter(content=seat).filter(state=True) and HourTime.objects.filter(start_time=time(int(start_time)))and Date.objects.filter(content=date)) == 0 :

            date1 = Date.objects.create(
                content = date,
                studycafe = studycafe
            )

            hour = HourTime.objects.create(
                date = date1,
                start_time = time(int(start_time)),
                use_time = time(int(use_time)),
                end_time = time(int(int(start_time) + int(use_time))),
                state = True
            )

            seat1 = Seats.objects.create(
                hour_time = hour,
                content = seat,
                state = True
            )

            Reservations.objects.create(
                personal_user = request.user,
                studycafe = studycafe,
                date = date1,
                hours = hour,
                seat = seat1,
            )
        else :
            print("사용시간 중복")

        return redirect('cafedetail', kwargs['pk'])


class ReviewView(generic.View) :

    def post(self, request, *args, **kwargs) :
        content = request.POST['review']
        studycafe = StudyCafe.objects.get(pk=kwargs['pk'])

        Review.objects.create(
            studycafe = studycafe,
            writer = request.user,
            content= content
        )
        return redirect('cafedetail', kwargs['pk'])