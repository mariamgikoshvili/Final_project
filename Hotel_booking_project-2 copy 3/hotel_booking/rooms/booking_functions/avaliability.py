import datetime
from rooms.models import Room, Booking


def check_avaliability(room, check_in, check_out):
    # True or False
    avail_list = []
    booking_list = Booking.objects.filter(room_id=room)
    if len(booking_list) > 0:
        for booking in booking_list:
            if booking.check_in >= check_out or booking.check_out <= check_in:
                avail_list.append(True)
            else:
                avail_list.append(False)
    else:
        avail_list.append(True)
    return False not in avail_list


