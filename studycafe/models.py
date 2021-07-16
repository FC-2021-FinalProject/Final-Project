from contextlib import contextmanager
from typing import ContextManager
from django.contrib.auth.models import User
from django.db import models

class PersonalUser(models.Model):
    # relationship
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='personal_user', null=True, blank=True)
    
    # model fields
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    email_authenticated = models.BooleanField(default=False)

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
    # is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Date(models.Model): 
    studycafe = models.ForeignKey(StudyCafe, on_delete=models.CASCADE, related_name='date', null=True, blank=True)
    content = models.TextField()

class HourTime(models.Model):
    date = models.ForeignKey(Date, on_delete=models.CASCADE, related_name='hour_time', null=True, blank=True )
    content = models.TextField()

class Seats(models.Model):
    hour_time = models.ForeignKey(HourTime, on_delete=models.CASCADE, related_name='seat', null=True,blank=True)
    content = models.TextField()

class Reservations(models.Model):
    personal_user = models.ManyToManyField(PersonalUser, related_name='reservation')
    studycafe = models.ForeignKey(StudyCafe, on_delete=models.CASCADE, related_name='reservation', null=True, blank=True)
  
    date = models.ForeignKey(Date, on_delete=models.CASCADE, related_name='reservation', null=True, blank=True)
    hour = models.ForeignKey(HourTime, on_delete=models.CASCADE, related_name='reservation', null=True, blank=True)
    seat = models.ForeignKey(Seats, on_delete=models.CASCADE, related_name='reservation', null=True, blank=True)

    state = models.TextField()
