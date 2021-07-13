from django.contrib import admin

from .models import PersonalUser, BusinessUser, StudyCafe, Reservation

# Register your models here.
admin.site.register(PersonalUser)
admin.site.register(BusinessUser)
admin.site.register(StudyCafe)
admin.site.register(Reservation)