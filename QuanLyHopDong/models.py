from django.db import models

# Create your models here.

class PhongBan(models.Model):
    maphongban = models.CharField(max_length=5, primary_key=True)
    tenphongban = models.CharField(max_length=50)

    def __str__(self):
        return self.tenphongban

class NhanVien(models.Model):
    manhanvien = models.CharField(max_length=5, primary_key=True)
    tennhanvien = models.CharField(max_length=50)
    cmnd = models.PositiveIntegerField()
    ngaysinh = models.DateField()
    gioitinh = models.BooleanField()
    diachi = models.CharField(max_length=50)
    sodienthoai = models.PositiveIntegerField()
    chucvu = models.CharField(max_length=50)
    maphongban = models.ForeignKey(PhongBan, on_delete=models.CASCADE)

    def __str__(self):
        return self.tennhanvien

class Tour(models.Model):
    matour = models.CharField(max_length=5, primary_key=True)
    tentour = models.CharField(max_length=50)
    madiadiem = models.ForeignKey(DiaDiem, related_name='madiadiemdi', on_delete=models.CASCADE)
    madiadiem = models.ForeignKey(DiaDiem, related_name='madiadiemden', on_delete=models.CASCADE)
    ngaybatdau = models.DateTimeField()
    ngayketthuc = models.DateTimeField()
    trangthaitour = models.CharField(max_length=50)

    def __str__(self):
        return self.tentour


class HopDong(models.Model):
    mahopdong = models.CharField(max_length=5, primary_key=True)
    ngayki = models.DateField()
    ngayhethang = models.DateField()
    giatrihopdong = models.FloatField()
    noidunghopdong = models.CharField(max_length=200)
    trangthaihopdong = models.CharField(max_length=50)
    manhanvien = models.ForeignKey(NhanVien, related_name='manhanvienlaphopdong', on_delete=models.CASCADE)
    makhachhang = models.CharField(max_length=5)
    maloaihopdong = models.CharField(max_length=5)
    matour = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self):
        return (self.mahopdong +'-'+ self.trangthaihopdong +'-'+ self.ngayhethang)
