from django.contrib import admin
from .models import PersonalUser, BusinessUser
# Register your models here.
admin.site.register(PersonalUser)
admin.site.register(BusinessUser)