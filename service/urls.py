from django.urls import path
from service.views import ReservationView

app_name = 'service'

urlpatterns = [
    path('reserve<int:pk>',ReservationView.as_view(), name='reservation'),
]