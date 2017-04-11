from django.http import HttpResponse
from django.shortcuts import render
from django.db import models

from QuanLyTour.models import DiaDiem,Tour,LoaiTour_Tour

# Create your views here.
def index(request):
     return render(request,"index.html",{})

def contact(request):
    Users = Tour.objects.all()
    context = {
        'Users':Users,
        }
    return render(request,"index-1.html",context)
def index2(request):
    return render(request,"index-2.html",{})
def index3(request):
    return render(request,"index-3.html",{})
def index4(request):
    return render(request,"index-4.html",{})
def tour1(request,matour):
    # matour= Tour.objects.get(matour = matour)
    # Users = Tour.objects.raw('SELECT * FROM QuanLyTour_tour where matour = %s',[matour])
    Users=Tour.objects.filter(matour=matour)
    context = {
        'Users':Users, 
        }
    return render(request,"tour1.html",context)
def tour(request):
    return render(request,"dattour.html",{})
def mientay(request):
    return render(request,"mientay.html",{})


