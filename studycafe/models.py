from contextlib import contextmanager
from typing import ContextManager
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

    def __str__(self) :
        return self.content

class HourTime(models.Model):
    date = models.ForeignKey(Date, on_delete=models.CASCADE, related_name='hour_time', null=True, blank=True )

    TIME_CHOICE = []
    for j in range(24) :
        if j < 10 :
            TIME_CHOICE.append(tuple([f'0{j}:00', f'0{j}:00']))
        else :
            TIME_CHOICE.append(tuple([f'{j}:00', f'{j}:00']))

    start_time = models.CharField(max_length=32)
    use_time = models.CharField(max_length=32)
    end_time = models.CharField(max_length=32)
    state = models.BooleanField(default=False)

    def __str__(self) :
        return (f"시작시간:{self.start_time}, 이용시간:{self.use_time}, 종료시간:{self.end_time}")

class Seats(models.Model):
    hour_time = models.ForeignKey(HourTime, on_delete=models.CASCADE, related_name='seat', null=True,blank=True)
    state = models.BooleanField(default=False)
    SEAT_CHOICE = []
    for i in range(1, 101) :
        SEAT_CHOICE.append(tuple([f'{i}', f'{i}']))

    content = models.CharField(max_length=32, choices=tuple(SEAT_CHOICE))

    def __str__(self) :
        return self.content

class Reservations(models.Model):
    personal_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='reservation')
    studycafe = models.ForeignKey(StudyCafe, on_delete=models.CASCADE, related_name='reservation', null=True, blank=True)
    date = models.ForeignKey(Date, on_delete=models.CASCADE, related_name='reservation', null=True, blank=True)
    hours = models.ForeignKey(HourTime, on_delete=models.CASCADE, related_name='reservation', null=True, blank=True)
    seat = models.ForeignKey(Seats, on_delete=models.CASCADE, related_name='reservation', null=True, blank=True)
    
class Review(models.Model):
# Review model realtionship
    studycafe = models.ForeignKey(StudyCafe, on_delete=models.CASCADE, related_name='review')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='writer', null=True, blank=True)
    content = models.TextField()
