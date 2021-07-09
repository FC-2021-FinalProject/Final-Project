from re import S
from studycafe.models import PersonalUser, StudyCafe
import studycafe
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic, View
from datetime import date, datetime

from service.models import Reservation

# Create your views here.
class ReservationView(generic.View) :
    model = Reservation
    template_name = 'cafedetail.html'
    context_object_name = 'reserv'

    # def get(self, request, *args, **kwargs) :
    #     context = {'reserv':get_object_or_404(Reservation)}
    #     return render(request, 'cafedetail.html', context)

    def post(self, request, *args, **kwargs) :
        date = request.POST['date']
        start_time = request.POST['start_time']
        time = request.POST['time']
        seat_type = request.POST['seat_type']
        studycafe = StudyCafe.objects.get(pk=kwargs['pk'])

        if date :
            if (start_time and time) :
                if seat_type :
                    Reservation.objects.create(
                        date = date,
                        start_time = start_time,
                        time = time,
                        seat_type = seat_type,
                        user = request.user,
                        studycafe = studycafe
                    )

        return redirect('cafedetail', kwargs['pk'])