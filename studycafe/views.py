# Standard Library Imports
from datetime import datetime, time
import os
from os import sched_get_priority_max
import requests, random, string

# Core Django Imports
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import request
from django.views import generic, View
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q

# Third-Party App Imports
import boto3
from boto3.session import Session
from urllib.parse import urlparse

from requests.api import get

# Imports from Apps
from config.settings import AWS_ACCESS_KEY_ID, AWS_S3_REGION_NAME, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, KAKAO_REST_API_KEY, KAKAO_SECRET_KEY,  KAKAO_APP_ADMIN_KEY, KAKAO_REDIRECT_URI, KAKAO_LOGOUT_REDIRECT_URI
from studycafe.models import  PersonalUser, BusinessUser, StudyCafe,CafeImage, Date, HourTime, Seats,  Reservations, Review, BookmarkedCafe


ERROR_MSG = {
    'ID_EXIST': '이미 존재하는 아이디 입니다.',
    'NO_EXIST_ID' : '존재하지 않는 아이디 입니다.',
    'MISSING_INPUT': '필수항목을 작성해주세요.',
    'PASSWORD_CHECK': '비밀번호를 확인해주세요',
    'PASSWORD_NOMATCH': '비밀번호가 일치하지 않습니다'
}
SUCCESS_MSG = {
    'PROFILE_UPDATED': '프로필이 변경되었습니다',
}

# S3 USING BOTO3
session = Session(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_S3_REGION_NAME,
        )
s3 = session.resource('s3')
now = datetime.now().strftime("%Y%H%M%S")
s3_url = 'https://django-s3-cj.s3.ap-northeast-2.amazonaws.com/'

def index(request):
    cafes = StudyCafe.objects.all()
    # print(cafes)
    # random_index = random.sample(range(0,len(cafes)), 4)

    # random_cafes = []
    # for i in random_index:
    #     print(i)
    #     random_cafes.append(cafes[random_index[i]])

    context = {'cafelists': cafes}
    return render(request, 'index.html', context)

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
    # if request.method == 'POST' :
    auth.logout(request)
    return redirect('index')

def kakao_login(request):
    REST_API_KEY=KAKAO_REST_API_KEY
    REDIRECT_URI=KAKAO_REDIRECT_URI
     
    return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code")

def kakao_callback(request):
#KEYS
    REST_API_KEY=KAKAO_REST_API_KEY
    SECRET_KEY=KAKAO_SECRET_KEY
    REDIRECT_URI=KAKAO_REDIRECT_URI

#GET CODE FOR ACCESS TOKEN REQUEST
    AUTHORIZATION_CODE=request.GET.get("code")

    response = requests.post(f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&code={AUTHORIZATION_CODE}&client_secret={SECRET_KEY}",headers={"Accept": "application/json"},)
    user_data = response.json()
    ACCESS_TOKEN = user_data['access_token']
    
#REQUEST TO GET KAKAO UNIQUE_ID INFORMATION
    url = "https://kapi.kakao.com/v2/user/me"
    headers = {"Authorization": "Bearer {}".format(user_data["access_token"])}
    response = requests.post(url, headers=headers)
    kakao_user = response.json()
    target_id = kakao_user['id']
    returning_user = PersonalUser.objects.filter(unique_id=target_id)

    if (len(returning_user) != 0):
        user = returning_user[0].user
        auth.login(request, user)
        return redirect('index')

    elif (len(returning_user) == 0):

        target_nickname = kakao_user['properties']['nickname']
        target_email = kakao_user['kakao_account']['email']        

        # SAVE PROFILE IMAGE FROM KAKAO PROFILE RESPONSE
        target_image_url = kakao_user['properties']['thumbnail_image']
        response = requests.get(target_image_url)
        
        if response.status_code == 200:
            img_data = response.content
            url_parser = urlparse(target_image_url)
            file_name = os.path.basename(url_parser.path)

            with open(file_name, 'wb') as new_file:
                new_file.write(img_data)
            
            data = open(file_name, 'rb')
            s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
                Key=now+file_name,
                Body=data
            )
            data.close()
            new_file.close()
            os.remove(file_name)
    
    # CREATE USER & PERSONAL USER INSTANCES
        user = User.objects.create_user(
            username=f"kakao{target_id}",
            email=target_email,
        )
        new_account = PersonalUser.objects.create(
            user=user,
            email=target_email,
            name=target_nickname,
            email_authenticated=True,
            unique_id=target_id,
            avatar=s3_url+now+file_name,
        )
        user.set_unusable_password()
        user.save()
        auth.login(request, user)
        return redirect('index')

    return redirect('index')

def kakao_logout(request):
# USING ACCESS TOKEN
    ACCESS_TOKEN=request.GET.get('access_token')
    url = "https://kauth.kakao.com/v1/user/logout"
    headers = {"Authorization": "Bearer {}".format(ACCESS_TOKEN)}

    response=requests.post(url, headers=headers)
   
    auth.logout(request)
  
    return redirect('index')


class PersonalUserDetailView(generic.DeleteView) :
    model = PersonalUser
    template_name = 'PUprofile.html'

    def get(self, request, *args, **kwargs) :
        puser = PersonalUser.objects.get(user=request.user)
        reserv_user = Reservations.objects.filter(personal_user=puser).order_by('-date')
        bookmarked = puser.bookmarked_cafe.all()
        context = {'puser': puser, 'bookmarked': bookmarked, 'reserv':reserv_user}
        return render(request, 'PUprofile.html', context)

    def post(self, request, *args, **kwargs) :
        return redirect('PUprofile', kwargs['username'])


def personal_profile_edit(request, username):
    
    validation_context  = {'profile': {'updated': False,'msg': '',}}

    if request.method == 'POST':
        user_name = request.POST['profile-name']
        user_username=request.POST['profile-username']
        user_email = request.POST['profile-email']
        user = User.objects.filter(username=username)
        

        file = request.FILES.get('profile-image')
        if file:
            s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
                Key=now+file.name,
                Body=file
            )
            new_avatar=s3_url+now+file.name

            PersonalUser.objects.filter(user=request.user).update(
                name=user_name,
                email=user_email,
                avatar=new_avatar,
            )
            user.update(
                username=user_username,
                email=user_email,
            )
        else: 
            PersonalUser.objects.filter(user=request.user).update(
                name=user_name,
                email=user_email,
            )
            user.update(
                username=user_username,
                email=user_email,
            )
        
        validation_context['profile']['updated'] = True
        validation_context['profile']['msg'] = SUCCESS_MSG['PROFILE_UPDATED']
        
        return render(request, 'PUprofile.html', validation_context)

    return redirect('PUprofile', request.user.username)


def personal_password_edit(request, username):

    validation_context  = {'error': {'state': False,'msg': '',}}

    if request.method == 'POST':
        user_password = request.POST['profile-password']
        password_check = request.POST['profile-password-check']
        user = User.objects.filter(username=username)
        
        if (user_password != password_check):
            validation_context['error']['state'] = True
            validation_context['error']['msg'] = ERROR_MSG['PASSWORD_NOMATCH']
            return render(request, 'PUprofile.html', validation_context)

        if (validation_context['error']['state'] is False):
            user.update(
                password=user_password,
            )

    return redirect('PUprofile', request.user.username)

class BusinessUserDetailView(generic.DetailView) :
    model = BusinessUser
    template_name = 'BUprofile.html'

    def get(self, request, *args, **kwargs) :
        buser = BusinessUser.objects.get(user=request.user)
        studycafes = StudyCafe.objects.filter(businessuser=buser)

        target_reviews=[]
        no_reviews=[]
        for studycafe in studycafes:
            reviews = Review.objects.filter(studycafe=studycafe)
            if (len(reviews)>0):
                target_reviews.append(reviews)
            else:
                no_reviews.append(studycafe)

        context = {'buser':buser, 'studycafes':studycafes,'target_reviews':target_reviews, 'no_reviews':no_reviews}
        return render(request, 'BUprofile.html', context)

    def post(self, request, *args, **kwargs) :
        return redirect('BUprofile', kwargs['pk'])

class BusinessUserEditView(View) :

    def get(self, request, *args, **kwargs) :
        buser = BusinessUser.objects.get(user=request.user)
        context = {'buser':buser}

        return render(request, 'BUedit.html', context)

    def post(self, request, *args, **kwargs) :
        name = request.POST.get('user_name')
        email = request.POST.get('email')

        BusinessUser.objects.filter(user=request.user).update(
            name=name,
            email=email
        )
        User.objects.filter(pk=kwargs['pk']).update(
            username=request.POST.get('user_name'),
            email = request.POST.get('email')
        )
        return redirect('BUprofile', kwargs['pk'])

class CafeListView(generic.ListView) :
    model = StudyCafe
    template_name = 'cafelist.html'
    context_object_name = 'cafelists'

    def post(self, request, *args, **kwargs) :
        return redirect('cafelist')


class CafeUploadView(View) :
    def get(self, request, *args, **kwargs) :
        businessuser = BusinessUser.objects.get(user=request.user)
        cafe = BusinessUser.objects.filter(studycafe__businessuser=businessuser)
        context = {'cafe':cafe}

        return render(request, 'cafeupload.html', context)

    def post(self, request, *args, **kwargs):
        representative_img = request.FILES.get('repre_image')
        file = request.FILES.getlist('image')
        for j in file :
            img_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
                Key=now+j.name,
                Body=j
            )
        businessuser = BusinessUser.objects.get(user=request.user)
        s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
                Key=now+representative_img.name,
                Body=representative_img
        )
        # for cafe features
        features_list = ['parking', 'drinks', 'wifi', 'printer', 'security']
        features_checked = self.request.POST.getlist('features')
        cafe_features = {
            'parking' : False,
            'drinks': False,
            'wifi': False,
            'printer': False,
            'security': False,
            }

        for feature in features_list:
            if feature in features_checked:
                cafe_features[f'{feature}'] = True
       
        cafe = StudyCafe.objects.create(
            name=request.POST['name'],
            businessuser = businessuser,
            address= request.POST.get('address'),
            price_per_hour = request.POST['price_per_hour'],
            business_hour_start = request.POST['business_hour_start'],
            business_hour_end = request.POST['business_hour_end'],
            representative_img = s3_url+now+representative_img.name,
            parking = cafe_features['parking'],
            drinks = cafe_features['drinks'],
            wifi = cafe_features['wifi'],
            printer = cafe_features['printer'],
            security = cafe_features['security'],
        )
        BookmarkedCafe.objects.create(
            studycafe=cafe
        )
        for i in file :
            CafeImage.objects.create(
                cafe=cafe,
                img = s3_url+now+i.name
            )
        return redirect('cafelist')

class CafeDetailView(generic.DetailView) :
    def get(self, request, *args, **kwargs) :
        cafe = get_object_or_404(StudyCafe, pk=kwargs['pk'])
        cafe_img = CafeImage.objects.filter(cafe=cafe)
        reviews = Review.objects.filter(studycafe=cafe)
        user = User.objects.get(username=request.user)
        

        is_bookmarked = False
        is_puser = False
        is_reserv = False
        try  :
            if (request.user.personal_user) in PersonalUser.objects.all() :
                is_puser = True
            if (request.user.personal_user in cafe.bookmark.users.all()):
                is_bookmarked = True
        except :
            pass
        context = {'cafe':cafe, 'reviews':reviews, 'cafe_img':cafe_img, 'is_bookmarked':is_bookmarked, 'is_puser':is_puser}

        return render(request ,'cafedetail.html', context)

class CafeEditView(generic.View) :
    model = StudyCafe
    template_name = 'cafeedit.html'

    def get(self, request, *args, **kwargs) :
        context = {'cafe':get_object_or_404(StudyCafe, pk=kwargs['pk'])}
        return render(request, 'cafeedit.html', context)

    def post(self, request, *args, **kwargs) :
        StudyCafe.objects.filter(pk=kwargs['pk']).update(
            name=request.POST['name'],
            address= request.POST.get('address'),
            price_per_hour = request.POST['price_per_hour'],
            business_hour_start = request.POST['business_hour_start'],
            business_hour_end = request.POST['business_hour_end'],
        )

        return redirect('cafedetail', kwargs['pk'])


def cafedelete(request, cafe_pk) :
    StudyCafe.objects.filter(pk=cafe_pk).update(
        is_deleted=True
    )
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
        end_time = int(start_time) + int(use_time)
        user = User.objects.get(username=request.user)
        puser = PersonalUser.objects.get(user=user)
        
        if len(Reservations.objects.filter(studycafe=studycafe, date__content=date, seat__content=seat)) != 0 :
            if len(Reservations.objects.filter(Q(hours__end_time__gt=start_time, hours__start_time__lt=end_time))) == 0 :
                date1 = Date.objects.create(
                    content = date,
                    studycafe = studycafe
                )

                hour = HourTime.objects.create(
                    studycafe = studycafe,
                    start_time = start_time,
                    end_time = end_time,
                )

                seat1 = Seats.objects.create(
                    studycafe = studycafe,
                    content = seat,
                    available = True
                )

                Reservations.objects.create(
                    personal_user = puser,
                    studycafe = studycafe,
                    date = date1,
                    hours = hour,
                    seat = seat1
                )
        else :
            date1 = Date.objects.create(
                content = date,
                studycafe = studycafe
            )

            hour = HourTime.objects.create(
                studycafe = studycafe,
                start_time = start_time,
                end_time = end_time,
            )

            seat1 = Seats.objects.create(
                studycafe = studycafe,
                content = seat,
                available = True
            )

            Reservations.objects.create(
                personal_user = puser,
                studycafe = studycafe,
                date = date1,
                hours = hour,
                seat = seat1
            )
    
        return redirect('cafedetail', kwargs['pk'])

        
class ReviewView(generic.View) :

    def post(self, request, *args, **kwargs) :
        content = request.POST['review']
        studycafe = StudyCafe.objects.get(pk=kwargs['pk'])
        # user = PersonalUser.objects.get(name=User.username)

        Review.objects.create(
            studycafe = studycafe,
            writer = request.user.personal_user,
            content= content
        )
        return redirect('cafedetail', kwargs['pk'])


def Payment(request):
    # url Collection
    actual_url = "https://pay.toss.im/api/v2/payments"
    testing_url = ""        # fake web that responds --> TOSS
    service_url = ""        # our service url

    apiKey = apiKey         # testkey for api
    retUrl = ""             # for successful redirection
    retCancelUrl = ""       # for failed redirection

    #Product information
    orderNo = 1                         # requires nonconflicting ascending order numbering
    payment_amount = 1000               # total price payed
    tax_free_amount = 0                 # Duty free amount
    amountTaxable = 0                   # actual price without VAT
    amountVat = 0                       # VAt amount
    productDesc = ""     # name of content purchased
    amountServiceFee = 0                # service fee
    expired_time = datetime.date()      # default is 10 mins but can be 60mins max      
    cashReceipt = True                  # Boolean value

    headers = { "Content-Type": "application/json"}
    params = {
        "orderNo":orderNo,                                       # 토스몰 고유의 주문번호 (필수)
        "amount":payment_amount,                                 # 결제 금액 (필수)
        "amountTaxFree":tax_free_amount,                         # 비과세 금액 (필수)
        "productDesc":productDesc,                               # 상품 정보 (필수)
        "apiKey":apiKey,                                         # 상점의 API Key (필수)
        "retUrl":f"{service_url}/ORDER-CHECK?orderno={orderNo}", # 결제 완료 후 연결할 웹 URL (필수)
        "retCancelUrl":f"{service_url}/close",                   # 결제 취소 시 연결할 웹 URL (필수)
        "autoExecute":true,                                      # 자동 승인 설정 (필수)
        "resultCallback":f"{service_url}/callback",              # 결제 결과 callback 웹 URL (필수-자동승인설정 true의 경우)
        "callbackVersion":"V2",                                  # callback 버전 (필수-자동승인설정 true의 경우)
        "amountTaxable":amountTaxable,                           # 결제 금액 중 과세금액
        "amountVat":amountVat,                                   # 결제 금액 중 부가세
        "amountServiceFee": amountServiceFee,                                    # 결제 금액 중 봉사료
        "expiredTime":expired_time,                     # 결제 만료 예정 시각
        "cashReceipt":cashReceipt,                               # 현금영수증 발급 가능 여부
        }

    response = requests.post(actual_url, headers=headers, params=params)
    # expected result for response:
    # {"code":0,"checkoutPage":"https://pay.toss.im/payfront/auth?payToken=test_token1234567890", 
    # "payToken":"example-payToken"}
    
    #after successful payment:
    # f"{service_url}/ORDER-CHECK?status=PAY_COMPLETE&orderNo={orderNo}&payMethod=TOSS_MONEY   
    # any status except for status=PAY_COMPLETE means unsuccesful payment

    #if status != PAY_COMPLETE:
    #    return
    

def IdPwSearch(request):
    return render(request, "IdPwSearch.html")


def IdSearch(request):
    result_msg = {'error': {'state': False, 'msg': ''}}
    
    if request.method == 'POST':

        verification_email == request.POST['verification-email1']

        if len(PersonalUser.objects.filter(email=verification_email)) != 0: 
            user_id = PersonalUser.objects.filter(email=verification_email).user.username
            partial_user_id = user_id[:4] + (len(user_id[3:])* '*')
            result_msg['error']['msg'] = partial_user_id

            return render(request, "IdPwSearch.html", result_msg)            

        elif len(BusinessUser.objects.filter(email=verification_email)) != 0 :
            user_id = BusinessUser.objects.filter(email=verification_email).user.username
            partial_user_id = user_id[:4] + (len(user_id[3:])* '*')
            result_msg['error']['msg'] = partial_user_id
        
            return render(request, "IdPwSearch.html", result_msg)            

        else:
            result_msg['error']['state'] = True
            result_msg['error']['msg'] = ERROR_MSG['NO_EXIST_ID']

            return render(request, "IdPwSearch.html", result_msg)
    
    return render(request, "IdPwSearch.html", result_msg)

def pw_random_generator(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    symbol = string.punctuation
    
    pw_parameters = lower + upper + digit + symbol
    
    temp = random.sample(pw_parameters, length)
    generated_pw = "".join(temp)
    
    return generated_pw

def PwSearch(request):
    result_msg = {'error': {'state': False, 'msg': ''}}

    if request.method == 'POST':
        verification_email == request.POST['verification-email2']
        user_id == request.POST['verification-id']

        if PersonalUser.objects.filter(email=verification_email).user == User.objects.filter(username=user_id):
            random_pw = pw_random_generator(16)
            filtered_user = User.objects.filter(username=user_id)
            filtered_user.objects.update(
                password = random_pw
            )
            # send pw to email()
            
            result_msg['error']['msg'] = "Your new password has been sent to your email."

            return render(request, "IdPwSearch.html", result_msg)
        
        if BusinessUser.objects.filter(email=verification_email).user == User.objects.filter(username=user_id):
            random_pw = pw_random_generator(16)
            filtered_user = User.objects.filter(username=user_id)
            filtered_user.objects.update(
                password = random_pw
            )
            # send pw to email()
            
            result_msg['error']['msg'] = "Your new password has been sent to your email."
    
            return render(request, "IdPwSearch.html", result_msg)
        
        else:
            result_msg['error']['state'] = True
            result_msg['error']['msg'] = "No matching user with that ID and email."

            return render ("IdPwSearch.html", result_msg)   

    return(request, "IdPwSearch.html", result_msg)


def bookmark(request, **kwargs):
    cafe_pk = kwargs['cafe_pk']
    target_cafe = StudyCafe.objects.filter(pk=cafe_pk).first()
    bookmark = BookmarkedCafe.objects.filter(studycafe__pk=target_cafe.pk).first()

    if request.user.personal_user in bookmark.users.all():
        bookmark.users.remove(request.user.personal_user)
        return redirect('cafedetail', cafe_pk)
         
    bookmark.users.add(request.user.personal_user)

    return redirect('cafedetail', cafe_pk)