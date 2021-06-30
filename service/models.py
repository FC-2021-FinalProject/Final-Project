from django.db.models.fields import NullBooleanField
from django.utils import tree
from userinfo.models import PeresnalUser
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from studycafe.models import StudyCafe
# Create your models here.
class Reservation(models.Model) :
    studycafe = models.ForeignKey(StudyCafe, on_delete=models.SET_NULL, related_name='reservation', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='reservation', null=True, blank=True)
    date = models.TextField()
    start_time = models.TextField()
    seat_type = models.TextField()
    state = models.TextChoices()
    time = models.TextChoices()

class Review(models.Model) :
    studycafe = models.ForeignKey(StudyCafe, on_delete=models.CASCADE, related_name='review')
    comment = models.TextField()
    writer = models.ForeignKey(PeresnalUser, on_delete=models.SET_NULL, related_name='writer', null=True, blank=True)
    star = models.TextChoices()

class Payment(models.Model) :
    reservation = models.ForeignKey(Reservation, on_delete=models.SET_NULL, related_name='payment', null=True, blank=True)
    status = models.TextChoices()

class Bookmark(models.Model) :
    studycafe = models.OneToOneField(StudyCafe, on_delete=models.CASCADE, related_name='bookmark')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='bookmark', null=True, blank=tree)

class Chatbot(models.Model) :
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='chatbot', null=True, blank=tree)
    studycafe = models.ForeignKey(StudyCafe, on_delete=models.CASCADE, related_name='chatbot')
    context = models.TextField()
    
class Notification(models.Model) :
    reservation = models.ForeignKey(Reservation, on_delete=models.SET_NULL, related_name='notification', null=True, blank=True)
    context = models.TextField()