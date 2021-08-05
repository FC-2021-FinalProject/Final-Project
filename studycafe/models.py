# Standard Library Imports
from contextlib import contextmanager
from typing import ContextManager
from datetime import date

# Core Django Imports
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import BooleanField


class PersonalUser(models.Model):
    # relationship
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='personal_user', null=True, blank=True)

    # model fields
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    email_authenticated = models.BooleanField(default=False)
    unique_id = models.IntegerField(null=True, blank=True)
    avatar = models.TextField()
    
    def __str__(self):
        return self.name


class BusinessUser(models.Model):
    # relationship
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='business_user', null=True, blank=True)
    
    # model fields
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    email_authenticated = models.BooleanField(default=False)
    registration_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class StudyCafe(models.Model) :
    #relationship
    businessuser = models.ForeignKey(BusinessUser, on_delete=models.SET_NULL, related_name='studycafe', null=True, blank=True)

    #model fields
    name = models.CharField(max_length=32)
    address = models.TextField()
    price_per_hour = models.PositiveIntegerField()
    business_hour_start = models.CharField(max_length=32)
    business_hour_end = models.CharField(max_length=32)
    img = models.TextField()
    
    parking = models.BooleanField(default=False)
    drinks = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    printer = models.BooleanField(default=False)
    security = models.BooleanField(default=False)

    def __str__(self):
        return self.name
      
class Date(models.Model): 
    studycafe = models.ForeignKey(StudyCafe, on_delete=models.CASCADE, related_name='date', null=True, blank=True)
    content = models.DateField()


class HourTime(models.Model):
    studycafe = models.ForeignKey(StudyCafe, on_delete=models.CASCADE, related_name='hours', null=True, blank=True)
    start_time = models.IntegerField()
    end_time = models.IntegerField()

    def __str__(self) :
        return (f"시작시간:{self.start_time}, 종료시간:{self.end_time}")


class Seats(models.Model):
    studycafe = models.ForeignKey(StudyCafe, on_delete=models.CASCADE, related_name='seat', null=True, blank=True)
    available = models.BooleanField(default=False)
    content = models.CharField(max_length=32)

    def __str__(self) :
        return self.content


class Reservations(models.Model):
    # relationship
    personal_user = models.ForeignKey(PersonalUser, on_delete=models.CASCADE,related_name='reservation', null=True, blank=True)
    studycafe = models.ForeignKey(StudyCafe, on_delete=models.CASCADE, related_name='reservation', null=True, blank=True)
    date = models.ForeignKey(Date, on_delete=models.CASCADE, related_name='reservation', null=True, blank=True)
    hours = models.ForeignKey(HourTime, on_delete=models.CASCADE, related_name='reservation', null=True, blank=True)
    seat = models.ForeignKey(Seats, on_delete=models.CASCADE, related_name='reservation', null=True, blank=True)
    
    
class Review(models.Model):
# Review model relationship
    studycafe = models.ForeignKey(StudyCafe, on_delete=models.CASCADE, related_name='review')
    writer = models.ForeignKey(PersonalUser, on_delete=models.SET_NULL, related_name='writer', null=True, blank=True)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)


class BookmarkedCafe(models.Model):
    studycafe = models.OneToOneField(StudyCafe, on_delete=models.CASCADE, related_name='bookmark', null=True, blank=True)
    users = models.ManyToManyField(PersonalUser, related_name="bookmarked_cafe", blank=True)