from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class PersonalUser(models.Model):
    # relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='persenal_user')
    
    # model fields
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    email_authenticated = models.BooleanField(default=False)

class BusinessUser(models.Model):
    # relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='business_user')
    
    # model fields
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    email_authenticated = models.BooleanField(default=False)
