# from studycafe.models import PersonalUser
# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.base import Model
# from studycafe.models import StudyCafe

# # model fields   
# class Payment(models.Model):
# # Payment model relationship
#     reservation = models.ForeignKey(Reservation, on_delete=models.SET_NULL, related_name='payment', null=True, blank=True)

# # model fields
#     status = models.TextChoices('status', 'complete None')

# class BookmarkedCafe(models.Model):
# # BookmarkedCafe models relationship
#     studycafe = models.OneToOneField(StudyCafe, on_delete=models.CASCADE, related_name='bookmark')
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='bookmark', null=True, blank=True)

# class Chatbot(models.Model) :
# # Chatbot models relationship
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='chatbot', null=True, blank=True)
#     studycafe = models.ForeignKey(StudyCafe, on_delete=models.CASCADE, related_name='chatbot')
# # model fields
#     context = models.TextField()
    
# class Notifications(models.Model):
# # Notifications model relationship
#     reservation = models.ForeignKey(Reservation, on_delete=models.SET_NULL, related_name='notification', null=True, blank=True)
# # model fields
#     context = models.TextField()