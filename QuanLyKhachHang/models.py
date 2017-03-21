from django.db import models
# Create your models here.
# Create: 19-03-2017
from QuanLyTour.models import Tour

class KhachHang(models.Model):
	makhachhang = models.CharField(max_length=5, primary_key=True)
	tenkhachhang = models.CharField(max_length=50)
	cmnd = models.PositiveIntegerField()
	ngaysinh = models.DateField()
	gioitinh = models.BooleanField()
	diachi = models.CharField(max_length=50)
	sodienthoai = models.PositiveIntegerField()
	tour = models.ManyToManyField(Tour, through='DatVe')
	def __str__(self):
		return self.makhachhang + " " + self.tenkhachhang

class PhuLucKhachHang(models.Model):
	maphuluckhachhang = models.CharField(max_length=5, primary_key=True)
	tenphuluckhachhang = models.CharField(max_length=50)
	cmnd = models.PositiveIntegerField()
	ngaysinh = models.DateField()
	gioitinh = models.BooleanField(default=True)
	sodienthoai = models.PositiveIntegerField()
	makhachhang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
	def __str__(self):
		return self.maphuluckhachhang + " " + self.tenphuluckhachhang

class DatVe(models.Model):
	matour = models.ForeignKey(Tour, on_delete=models.CASCADE)
	makhachhang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
	tennhanvien = models.CharField(max_length=50)
	soluongvedat = models.PositiveIntegerField(default=0)
	thanhtien = models.FloatField(default=0)
