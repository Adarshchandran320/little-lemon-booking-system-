from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date
from .models import Booking
from .forms import BookingForm
import json


def home(request):
    return render(request, 'index.html')


def about(request):
    """Render the about page"""
    return render(request, 'about.html')


def menu(request):
    """Render the menu page"""
    return render(request, 'menu.html')


def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book')
    
    context = {'form': form}
    return render(request, 'book.html', context)


def reservations(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings.html', {'bookings': bookings})


def bookings_json(request):
    date = request.GET.get('date')
    if date:
        bookings = Booking.objects.filter(reservation_date=date)
    else:
        bookings = Booking.objects.all()
    
    booking_list = []
    for booking in bookings:
        booking_dict = {
            'first_name': booking.first_name,
            'reservation_date': str(booking.reservation_date),
            'reservation_slot': booking.reservation_slot
        }
        booking_list.append(booking_dict)
    
    return JsonResponse({'bookings': booking_list})
