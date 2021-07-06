from django.contrib import admin

from .models import PersonalUser, BusinessUser
from .models import StudyCafe

# Register your models here.
admin.site.register(PersonalUser)
admin.site.register(BusinessUser)
admin.site.register(StudyCafe)