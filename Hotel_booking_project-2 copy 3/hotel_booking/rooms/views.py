from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, FormView, DetailView, DeleteView
from .models import Hotel, Room, Booking
from .forms import AvaliabilityForm
from rooms.booking_functions.avaliability import check_avaliability
from datetime import datetime
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'rooms/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('hotellist')
    
    
class RegisterPage(FormView):
  template_name = 'rooms/register.html'
  form_class = UserCreationForm
  success_url = reverse_lazy('home')


  def form_valid(self, form):
    user = form.save()

    if user is not None:
      login(self.request, user)
      return super(RegisterPage, self).form_valid(form)
    
class HomeView(ListView):
    model = Hotel
    template_name = 'home.html'
    context_object_name = 'top_hotels'
    # ordering = ['-rating']
    
    def get_queryset(self):
         return Hotel.objects.order_by('-rating')[:3]



class Hotellist(ListView):
    model = Hotel
    template_name = 'hotel_list.html'
    context_object_name = 'hotels'

class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'rooms/hotel_detail.html'
    context_object_name = 'hotel'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['rooms'] = Room.objects.filter(hotel = self.object)
        return context

class RoomDetailsView(DetailView):
    model = Room
    template_name = 'rooms/room_detail.html'
    context_object_name = 'room'


class Bookinglist(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'rooms/booking_list.html'
    context_object_name = 'booking_list'
    paginate_by = 5

    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
        

class BookingView(LoginRequiredMixin, FormView):
    form_class= AvaliabilityForm
    template_name = 'avaliability_form.html'
    success_url = reverse_lazy('hotel_detail')

    def form_valid(self, form):
        data = form.cleaned_data
        room_id = self.kwargs['pk']
        room = get_object_or_404(Room, pk=room_id)

        if check_avaliability(room.pk, data['check_in'], data['check_out']):
            diff = data['check_out'] - data['check_in']
            diff_days = diff.days
            total_price = diff_days * room.price
            booking = Booking.objects.create(
                user = self.request.user,
                room = room,
                check_in = data['check_in'],
                check_out = data['check_out'],
                total_price = total_price
            )
            booking.save()
            messages.success(self.request, 'Your reservation has been confirmed!')
            return redirect(reverse('hotellist'))
        else:
            messages.info(self.request, 'The room is not available on these dates!')
            return HttpResponseRedirect(reverse('bookingview', kwargs={'pk': room_id}))

            

class BookingDelete(LoginRequiredMixin, DeleteView):
  model = Booking
  context_object_name = 'booking'
  success_url = reverse_lazy('bookinglist')
