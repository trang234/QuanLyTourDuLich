# -*- encoding: utf-8 -*-

from django.db import models
from QuanLyNhanVien.models import NhanVien
# from QuanLyKhachHang.models import KhachHang
from QuanLyTour.models import Tour
# Create your models here.


class HopDong(models.Model):
    mahopdong = models.CharField(
        max_length=5, 
        verbose_name="Mã Hợp đồng",
        primary_key=True)


    def Autoid(self):
        mahopdong = "HD" + models.AutoField()
        super(HopDong, self).Autoid()

    

    maloaihopdong = models.CharField(
        max_length=5,
        verbose_name="Mã Loại Hợp đồng")

    ngayki = models.DateField(verbose_name="Ngày Ký")

    ngayhethang = models.DateField(verbose_name="Ngày Hết Hạng")

    giatrihopdong = models.FloatField(verbose_name="Giá Trị Hợp Đồng")

    noidunghopdong = models.CharField(max_length=200,verbose_name="Nội Dung Hợp đồng", null = True)

    trangthaihopdong = models.CharField(
        max_length=50,
        verbose_name="Trạng Thái Hợp đồng",
        null = True)


    manhanvien = models.ForeignKey(NhanVien, 
        related_name='manhanvienlaphopdong', 
        verbose_name="Mã Nhân Viên",
        on_delete=models.CASCADE)
    # makhachhang = models.CharField(max_length=5)

    # matour = models.ForeignKey(Tour, verbose_name="Mã Tour",on_delete=models.CASCADE)

    def __str__(self):
        # return (self.mahopdong + " " + self.trangthaihopdong + " " + self.ngayhethang)
        return (self.maloaihopdong)
