from django.shortcuts import render, redirect
from AmbulanceApp.models import User
from AmbulanceApp.models import Ambulance


# Create your views here.


def user_register(request):
    if request.method == 'POST':
        user = User(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                    username=request.POST['username'], password=request.POST['password'])
        user.save()
        return redirect('/user_login')
    else:
        return render(request, 'user_register.html')


def user_login(request):
    return render(request, 'user_login.html')


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def ambulance(request):
    return render(request, 'ambulances.html')


def booked(request):
    return render(request, 'booked_ambulances.html')


def hospitals(request):
    return render(request, 'nearby_hospitals.html')


def services(request):
    return render(request, 'services.html')


def update_profile(request):
    return render(request, 'update_profile.html')


def ambulance_register(request):
    if request.method == 'POST':
        ambulance_driver = Ambulance(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                                     username=request.POST['username'], password=request.POST['password'])
        ambulance_driver.save()
        return redirect('/ambulance_login')
    else:
        return render(request, 'ambulance_register.html')


def ambulance_login(request):
    return render(request, 'ambulance_login.html')


def booking_request(request):
    return render(request, 'booking_request.html')


def emergency_booking(request):
    return render(request, 'emergency_booking.html')


def ambulance_status(request):
    return render(request, 'ambulance_status.html')


def near_hospitals(request):
    return render(request, 'near_hospitals.html')


def driver_profile(request):
    return render(request, 'driver_profile.html')


