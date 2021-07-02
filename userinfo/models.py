from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class PeresnalUser(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='persenal_user',null=True, blank=True)
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    email_authenticated = models.BooleanField(default=False)

class BusinessUser(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='business_user',null=True, blank=True)
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    email_authenticated = models.BooleanField(default=False)