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
    state = models.BooleanField(default=False)
    time = models.TextField()

    TIME_CHOICE = (
        ('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'),('20:00', '20:00'),
    )

    SEAT_CHOICE = (
        ('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd'), ('e', 'e'), ('f', 'f'), ('g', 'g'), ('h', 'h'), ('i', 'i'), ('j', 'j'), ('k', 'k'), ('l', 'l'), ('m', 'm'), ('n', 'n'), ('o', 'o'), ('p', 'p'), ('q', 'q'), ('r', 'r'), ('s', 's'), ('t', 't'), ('u', 'u'), ('v', 'v'), ('w', 'w'), ('x', 'x'), ('y', 'y'), ('z', 'z'),
    )
    start_time = models.CharField(max_length=32, choices=TIME_CHOICE)
    seat_type = models.CharField(max_length=32, choices=SEAT_CHOICE)


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