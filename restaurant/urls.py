from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book, name='book'),
    path('reservations/', views.reservations, name='reservations'),
    path('bookings/', views.bookings_json, name='bookings_json'),
]
