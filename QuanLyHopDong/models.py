from django.db import models
from QuanLyNhanVien.models import NhanVien
# from QuanLyKhachHang.models import KhachHang
from QuanLyTour.models import Tour
# Create your models here.

class HopDong(models.Model):
    mahopdong = models.CharField(
        max_length=5, 
        primary_key=True)

    maloaihopdong = models.CharField(max_length=5)
    ngayki = models.DateField()
    ngayhethang = models.DateField()
    giatrihopdong = models.FloatField()
    noidunghopdong = models.CharField(max_length=200)
    trangthaihopdong = models.CharField(max_length=50)
    manhanvien = models.ForeignKey(NhanVien, related_name='manhanvienlaphopdong', on_delete=models.CASCADE)
    # makhachhang = models.CharField(max_length=5)
    matour = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self):
        return (self.mahopdong +'-'+ self.trangthaihopdong +'-'+ self.ngayhethang)
