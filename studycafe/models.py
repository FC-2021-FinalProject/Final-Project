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
        return self.user.username

class BusinessUser(models.Model):
    # relationship
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='business_user', null=True, blank=True)
    
    # model fields
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    email_authenticated = models.BooleanField(default=False)
    registration_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username

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