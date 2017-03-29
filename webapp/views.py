from django.http import HttpResponse
from django.shortcuts import render

from .models import DiaDiem,Tour

# Create your views here.
def index(request):
     return render(request,"index.html",{})

def contact(request):
    Users = DiaDiem.objects.all()
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
def tour1(request,madiadiem):
    madiadiem= DiaDiem.objects.get(madiadiem=madiadiem)
    Users = DiaDiem.objects.raw('SELECT madiadiem,tendiadiem FROM webapp_diadiem where madiadiem = %s',[madiadiem])
    context = {
        'Users':Users, 
        }
    return render (request,"tour1.html",context)
def tour(request):
    return render(request,"dattour.html",{})

