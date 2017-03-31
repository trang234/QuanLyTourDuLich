# -*- coding: utf8 -*-

from django.db import models
from QuanLyNhanVien.models import NhanVien
from QuanLyKhachHang.models import KhachHang
from QuanLyTour.models import Tour
import random
import datetime
# now = datetime.datetime.now()
# Create your models here.
    

class HopDong(models.Model):
    mahopdong = models.AutoField(
        # default = ('HD%s%s%s%s%s%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)),
        # default = ('HD%s' % (random.randrange(0, 101, 2))),

        # max_length = 100, 
        verbose_name="Mã Hợp đồng",
        primary_key=True)
    

    # maloaihopdong = models.CharField(
    #     max_length=5,
    #     verbose_name="Mã Loại Hợp đồng")

    ngayki = models.DateField(verbose_name="Ngày Ký")

    ngayhethang = models.DateField(verbose_name="Ngày Hết Hạng")

    giatrihopdong = models.FloatField(default = 0 ,verbose_name="Giá Trị Hợp Đồng")

    noidunghopdong = models.CharField(max_length=200,verbose_name="Nội Dung Hợp đồng", null = True)

    

    trangthaihd_choices = (
        ("Dang duyet", "Dang duyet"),
        ("Da ky", "Da ky"),
        )

    trangthaihopdong = models.CharField(
        max_length=20,
        choices = trangthaihd_choices,
        default="",
        verbose_name="Trạng thái")


    manhanvien = models.ForeignKey(NhanVien, 
        related_name='manhanvienlaphopdong', 
        verbose_name="Mã Nhân Viên",
        on_delete=models.CASCADE)


    makhachhang = models.ForeignKey(KhachHang,
        related_name='khachhangkihopdong', 
        default = '',
        verbose_name="Mã Khách Hàng",
        on_delete=models.CASCADE)

    matour = models.ForeignKey(Tour, verbose_name="Mã Tour",on_delete=models.CASCADE)

    
    def __str__(self):
        # return (self.mahopdong + " " + self.trangthaihopdong + " " + self.ngayhethang)
        return (self.mahopdong + " - " + self.trangthaihopdong)
