from django.db import models
from userinfo.models import BusinessUser

class StudyCafe(models.Model) :
    businessuser = models.ForeignKey(BusinessUser, on_delete=models.SET_NULL, related_name='studycafe', null=True, blank=True)
    name = models.CharField(max_length=32)
    address = models.TextField()
    price_per_hour = models.CharField
    business_hour_start = models.CharField(max_length=32)
    business_hour_end = models.CharField(max_length=32)
    img = models.TextField()