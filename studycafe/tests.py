from django.test import TestCase
# Q = StudyCafe.objects.filter(name=studycafe, date__content=date)
# D = Date.objects.filter(studycafe=studycafe, content=date, hour_time__start_time=i)
# K = HourTime.objects.filter(date=D, start_time=i)
if len(StudyCafe.objects.filter(name=studycafe.name).filter(date__content=date)) == 0 :
            date2=Date.objects.create(
                content=date,
                studycafe=studycafe
            )
            print('1단계 날짜 안겹침')
            
        else :
            date1 = StudyCafe.objects.filter(name=studycafe.name).filter(date__content=date)
            date2 = Date.objects.filter(content=date, studycafe=studycafe)
            print('1단계 날짜 겹침')
            print(date1)
            print(date2)
        i = [i for i in range(int(start_time), int(start_time) + int(use_time))]
        # for i in range(int(start_time), int(start_time) + int(use_time)) :
            print(i)
            # if len(get_object_or_404(StudyCafe, pk=kwargs['pk'], date__content=date, hour_time__start_time=i)) == 0 :
        # if len(get_object_or_404(StudyCafe, pk=kwargs['pk'], date__hour_time__start_time=i)) == 0 : 
        if get_or_none() :
                hour1 = HourTime.objects.create(
                    date = date1,
                    start_time = start_time,
                    use_time = use_time,
                    end_time = end_time
                )
            print('예약 가능 - 2단계 시간 중복 X')
            if hour1.get():
                seat1 = Seats.objects.create(
                    hour_time=hour1,
                    content=seat,
                    available=True
                )
                print('예약 가능 - 3단계 좌석 중복 X')
                Reservations.objects.create(
                        personal_user=request.user,
                        studycafe=studycafe,
                        date = date1,
                        hours = hour1,
                        seat = seat1
                    )
            else :
                print('예약 불가능 - 3단계 좌석 중복')
        else :
            hour1 = get_object_or_404(date1.filter(hour_time__start_time=i))
            print('예약 불가능 - 2단계 시간 중복 ')
            if len(hour1.get(seat__content=seat)) == 0 :
                    seat1 = Seats.objects.create(
                        hour_time=hour1,
                        content=seat,
                        available=True 
                        )
                    print('예약 가능 - 3단계 좌석 중복 X')
                    Reservations.objects.create(
                        personal_user=request.user,
                        studycafe=studycafe,
                        date = date1,
                        hours = hour1,
                        seat = seat1
                    )
            else:
                print('예약 불가능 - 3단계 좌석 중복')

                # new_range = get_range(new_reservation)
                 # if (not non_unique_reservation):
            #     new_reservation.save()
            # J = HourTime.objects.filter(reservation__studycafe=studycafe, date__content=date, seat__content=seat)
            # K = J.filter(end_time__range=[time(int(start_time)), end_time])
if Reservations.objects.filter(hours__start_time__lt=start_time, hours__start_time__lte=end_time, hours__end_time__gte=start_time, hours__end_time__) :