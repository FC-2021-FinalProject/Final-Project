from django.http import request
from django.views import View
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.views import generic
from boto3.session import Session
import boto3
from config.settings import AWS_ACCESS_KEY_ID, AWS_S3_REGION_NAME, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME
from datetime import date, datetime
from studycafe.models import StudyCafe


class CafeListView(generic.ListView) :
    model = StudyCafe
    template_name = 'cafelist.html'
    context_object_name = 'cafelists'

    # def get(self, request, *args, **kwargs) :
    #     return render(request, 'cafelist.html')

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
    template_name = 'cafedetail.html'
    context_object_name = 'cafe'

    def post(self, request, *args, **kwargs) :


        return redirect('studycafe:cafedetail')