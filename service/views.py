from django.shortcuts import redirect, render
from django.views import generic, View
from datetime import date, datetime

from service.models import Reservation
from studycafe.models import StudyCafe

# Create your views here.
class ReservationView(generic.View) :
    model = Reservation
    template_name = 'cafedetail.html'
    context_object_name = 'reserv'

    def post(self, request, *args, **kwargs) :
        date = request.POST['date']
        start_time = request.POST['start_time']
        time = request.POST['time']
        seat_type = request.POST['seat_type']
        studycafe = StudyCafe.objects.get(pk=kwargs['pk'])
        state = Reservation.objects.filter(state=False).update(state=True)

        # is_valid ?
        if date :
            if (start_time and time) :
                if seat_type :
                    Reservation.objects.create(
                        date = date,
                        start_time = start_time,
                        time = time,
                        seat_type = seat_type,
                        user = request.user,
                        studycafe = studycafe,
                        state = state
                    )

        return redirect('cafedetail', kwargs['pk'])