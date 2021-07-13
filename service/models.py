from studycafe.models import PersonalUser
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from studycafe.models import StudyCafe

class Reservation(models.Model):
#Reservation model relationship
    studycafe = models.ForeignKey(StudyCafe, on_delete=models.SET_NULL, related_name='reservation2', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='reservation2', null=True, blank=True)

#model fields
    date = models.TextField()
    state = models.BooleanField(default=False)
    time = models.TextField()

    TIME_CHOICE = []
    for j in range(24) :
        if j < 10 :
            TIME_CHOICE.append(tuple([f'0{j}:00', f'0{j}:00']))
        else :
            TIME_CHOICE.append(tuple([f'{j}:00', f'{j}:00']))

    SEAT_CHOICE = []
    for i in range(1, 101) :
        SEAT_CHOICE.append(tuple([f'{i}', f'{i}']))
    start_time = models.CharField(max_length=32, choices=tuple(TIME_CHOICE))
    seat_type = models.CharField(max_length=32, choices=tuple(SEAT_CHOICE))

class Review(models.Model):
# Review model realtionship
    studycafe = models.ForeignKey(StudyCafe, on_delete=models.CASCADE, related_name='review')
    writer = models.ForeignKey(PersonalUser, on_delete=models.SET_NULL, related_name='writer', null=True, blank=True)

# model fields   
    comment = models.TextField()
    star = models.TextField()

class Payment(models.Model):
# Payment model relationship
    reservation = models.ForeignKey(Reservation, on_delete=models.SET_NULL, related_name='payment', null=True, blank=True)

# model fields
    status = models.TextChoices('status', 'complete None')

class BookmarkedCafe(models.Model):
# BookmarkedCafe models relationship
    studycafe = models.OneToOneField(StudyCafe, on_delete=models.CASCADE, related_name='bookmark')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='bookmark', null=True, blank=True)

class Chatbot(models.Model) :
# Chatbot models relationship
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='chatbot', null=True, blank=True)
    studycafe = models.ForeignKey(StudyCafe, on_delete=models.CASCADE, related_name='chatbot')
# model fields
    context = models.TextField()
    
class Notifications(models.Model):
# Notifications model relationship
    reservation = models.ForeignKey(Reservation, on_delete=models.SET_NULL, related_name='notification', null=True, blank=True)
# model fields
    context = models.TextField()