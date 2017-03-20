from django.http import HttpResponse
from django.shortcuts import render

from .models import KhachHang

# Create your views here.
def index(request):
     return render(request,"index.html",{})

def contact(request):
	Users = KhachHang.objects.all()
	data = {'Users' : Users, 'Hihi' : 'Hihi'}
	return render(request,"index-1.html",data)
def index2(request):
	return render(request,"index-2.html",{})
def index3(request):
	return render(request,"index-3.html",{})
def index4(request):
	return render(request,"index-4.html",{})
def tour1(request):
	return render(request,"tour1.html",{})
def tour(request):
	return render(request,"dattour.html",{})

