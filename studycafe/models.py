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

# PositiveIntegerField MEMO
# Like an IntegerField, but must be either positive or zero (0). Values from 0 to 2147483647 are safe in all databases supported by Django. The value 0 is accepted for backward compatibility reasons.

class Reservation(models.Model):
#Reservation model relationship
    studycafe = models.ForeignKey(StudyCafe, on_delete=models.SET_NULL, related_name='reservation', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='reservation', null=True, blank=True)

#model fields
    date = models.TextField()
    state = models.BooleanField(default=False)
    time = models.IntegerField()
    end_time = models.TextField()

    TIME_CHOICE = []
    for j in range(24) :
        if j < 10 :
            TIME_CHOICE.append(tuple([f'0{j}:00', f'0{j}:00']))
        else :
            TIME_CHOICE.append(tuple([f'{j}:00', f'{j}:00']))

    SEAT_CHOICE = []
    for i in range(1, 101) :
        SEAT_CHOICE.append(tuple([f'{i}', f'{i}']))

    start_time = models.CharField(max_length=32, choices=tuple(TIME_CHOICE))
    seat_type = models.CharField(max_length=32, choices=tuple(SEAT_CHOICE))

