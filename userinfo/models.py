from django.db import models

# Create your models here.
class PeresnalUser(models.Model) :
    name = models.CharField(max_length=32)

class BusinessUser(models.Model) :
    name = models.CharField(max_length=32)