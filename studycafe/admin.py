from django.contrib import admin

from .models import PersonalUser, BusinessUser, StudyCafe, Reservations, Date, HourTime, Seats

# Register your models here.
admin.site.register(PersonalUser)
admin.site.register(BusinessUser)
admin.site.register(StudyCafe)
admin.site.register(Reservations)
admin.site.register(Date)
admin.site.register(HourTime)
admin.site.register(Seats)