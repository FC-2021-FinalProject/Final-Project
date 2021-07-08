from django.utils import tree
from studycafe.models import PersonalUser
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from studycafe.models import StudyCafe

class Reservation(models.Model):
#Reservation model relationship
    studycafe = models.ForeignKey(StudyCafe, on_delete=models.SET_NULL, related_name='reservation', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='reservation', null=True, blank=True)

#model fields
    date = models.TextField()
    start_time = models.TextField()
    seat_type = models.TextField()
    state = models.TextChoices()
    time = models.TextChoices()

class Review(models.Model):
# Review model realtionship
    studycafe = models.ForeignKey(StudyCafe, on_delete=models.CASCADE, related_name='review')
    writer = models.ForeignKey(PersonalUser, on_delete=models.SET_NULL, related_name='writer', null=True, blank=True)

# model fields   
    comment = models.TextField()
    star = models.TextChoices()

class Payment(models.Model):
# Payment model relationship
    reservation = models.ForeignKey(Reservation, on_delete=models.SET_NULL, related_name='payment', null=True, blank=True)

# model fields
    status = models.TextChoices()

class BookmarkedCafe(models.Model):
# BookmarkedCafe models relationship
    studycafe = models.OneToOneField(StudyCafe, on_delete=models.CASCADE, related_name='bookmark')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='bookmark', null=True, blank=tree)

class Chatbot(models.Model) :
# Chatbot models relationship
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='chatbot', null=True, blank=tree)
    studycafe = models.ForeignKey(StudyCafe, on_delete=models.CASCADE, related_name='chatbot')
# model fields
    context = models.TextField()
    
class Notifications(models.Model):
# Notifications model relationship
    reservation = models.ForeignKey(Reservation, on_delete=models.SET_NULL, related_name='notification', null=True, blank=True)
# model fields
    context = models.TextField()