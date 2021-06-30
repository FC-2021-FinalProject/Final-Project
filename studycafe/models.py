from django.db import models

class StudyCafe(models.Model) :
    businessuser = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    address = models.TextField()
    price_per_hour = models.CharField
    business_hour_start = models.CharField(max_length=32)
    business_hour_end = models.CharField(max_length=32)
    img = models.TextField()