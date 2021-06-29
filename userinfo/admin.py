from django.contrib import admin
from .models import PeresnalUser, BusinessUser
# Register your models here.
admin.site.register(PeresnalUser)
admin.site.register(BusinessUser)