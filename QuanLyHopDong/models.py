# -*- coding: utf8 -*-

from django.db import models
from QuanLyNhanVien.models import NhanVien
from QuanLyKhachHang.models import KhachHang
from QuanLyTour.models import Tour
import datetime
now = datetime.datetime.now()
# Create your models here.
    

class HopDong(models.Model):
    mahopdong = models.CharField(
        default = ('HD%s%s%s%s%s%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)),
        max_length = 100, 
        verbose_name="Mã Hợp đồng",
        primary_key=True)
    
    manhanvien = models.ForeignKey(NhanVien,  
        verbose_name = "Mã NV",
        on_delete = models.CASCADE)


    # makhachhang = models.ForeignKey(KhachHang,
    #     related_name='khachhangkihopdong', 
    #     verbose_name="Mã KH",
    #     on_delete=models.CASCADE)

    # matour = models.ForeignKey(Tour,
    #     related_name='matourdat', 
    #     verbose_name="Mã Tour",
    #     on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.mahopdong =  'HD%s%s%s%s%s%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)
        return super(HopDong, self).save(*args, **kwargs)

    ngayki = models.DateField(verbose_name="Ngày Ký")

    ngayhethang = models.DateField(verbose_name="Ngày Hết Hạng")

    giatrihopdong = models.FloatField(default = 0 ,verbose_name="Giá Trị Hợp Đồng")

    noidunghopdong = models.CharField(max_length=200,verbose_name="Nội Dung Hợp đồng", null = True)

    # DD, DK, TPX = 0, 1, 2
    tour = Tour(models.Model)

    trangthaitour =  getattr(tour, "trangthai") 

    trangthaihopdong = models.CharField(
        max_length=20,
        default="Đang duyệt",
        verbose_name="Trạng thái")

    def save(self, *args, **kwargs):
        if trangthaitour == "Đã đi":
            self.trangthaihopdong = 'Thu phí xong'
        elif trangthaitour == "Chưa đi":
            self.trangthaihopdong = 'Đã ký'
        super(HopDong, self).save(*args, **kwargs)

    
    
    def __str__(self):
        return ('%s' % self.mahopdong + " - " + self.trangthaihopdong )

    