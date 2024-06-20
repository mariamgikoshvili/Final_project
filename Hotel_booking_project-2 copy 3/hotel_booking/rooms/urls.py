from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('hotels/', views.Hotellist.as_view(), name = 'hotellist'),
    path('bookings/', views.Bookinglist.as_view(), name = 'bookinglist'),
    path('book/<int:pk>/', views.BookingView.as_view(), name = 'bookingview'),
    path('<int:pk>/', views.HotelDetailView.as_view(), name = 'hotel_detail'),
    path('hotel/<int:pk>/', views.RoomDetailsView.as_view(), name = 'room_detail'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('booking_delete/<int:pk>/', views.BookingDelete.as_view(), name='booking_delete')
]

