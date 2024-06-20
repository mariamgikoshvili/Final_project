from typing import Iterable
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

# Create your models here.

class Hotel(models.Model):
    city = models.CharField(default=None, max_length=64)
    name = models.CharField(default=None, max_length=64)
    address = models.CharField(default=None, max_length=64)
    overview = models.CharField(default=None, max_length=64)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    def __str__(self):
       return f"{self.name} in {self.city}"


class Room(models.Model):
    room_category = (
        ('Single' , 'Single room'),
        ('Standard double','Standard double room'),
        ('Deluxe double','Deluxe double room'),
        ('Studio','Studio room or apartment'),
        ('Suite','Junior suite'),
        ('Presidential suite','Presidential suite')
    )
    number = models.IntegerField()
    category = models.CharField(max_length=24, choices=room_category)
    beds = models.IntegerField()
    price = models.PositiveIntegerField()
    capacity = models.IntegerField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
       return f'{self.category} in {self.hotel} for {self.capacity} people.'


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.PositiveBigIntegerField(null=False, default=0)


    def __str__(self):
      return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out} for ${self.total_price}.'