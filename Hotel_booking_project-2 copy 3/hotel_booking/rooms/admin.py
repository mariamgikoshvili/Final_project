from django.contrib import admin
from .models import Room, Hotel, Booking

# Register your models here.

admin.site.register(Room)
admin.site.register(Hotel)
admin.site.register(Booking)
