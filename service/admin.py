from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Reservation)
admin.site.register(Review)
admin.site.register(Payment)
admin.site.register(Bookmark)
admin.site.register(Chatbot)
admin.site.register(Notification)