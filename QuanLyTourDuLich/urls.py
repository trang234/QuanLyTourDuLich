"""QuanLyTourDuLich URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url,include
from django.contrib import admin
from webapp import views
from django.conf.urls.static import static

urlpatterns = [
	url(r'^QuanLyTour/', include('QuanLyTour.urls')),
    url(r'^QuanLyNhanVien/', include('QuanLyNhanVien.urls')),
    url(r'^$',views.index, name='index.html'),
    url(r'^contact/$',views.contact, name='index-1.html'),
    url(r'^index2/$',views.index2, name='index-2.html'),
    url(r'^index3/$',views.index3, name='index-3.html'),
    url(r'^index4/$',views.index4, name='index-4.html'),
    url(r'^tour1/(?P<madiadiem>[0-9]+)/$', views.tour1, name='tour1.html'),
    url(r'^tour/$',views.tour, name='dattour.html') ,
    url(r'^admin/', include(admin.site.urls)),
]
