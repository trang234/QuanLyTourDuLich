from django.db import models
from QuanLyKhachHang.models import KhachHang
from QuanLyTour.models import Tour

# Create your models here.
class KhachHang_Tour(models.Model):
	matour = models.ForeignKey(Tour, on_delete=models.CASCADE)
	makhachhang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
	soluongvedat = models.PositiveIntegerField()
	thanhtien = models.FloatField()
