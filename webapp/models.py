from django.db import models

# Create your models here.
# Create: 19-03-2017
class DiaDiem(models.Model):
    madiadiem = models.CharField(max_length=5, primary_key=True)
    tendiadiem = models.CharField(max_length=50)
    mota = models.CharField(max_length=100)
    imgpath = models.CharField(max_length=100)
    def __str__(self):
        return self.madiadiem 
    
class Tour(models.Model):
    matour = models.CharField(max_length=5, primary_key=True)
    tentour = models.CharField(max_length=50)
    madiadiem = models.ForeignKey(DiaDiem, related_name='madiadiemdi', on_delete=models.CASCADE)
    madiadiem = models.ForeignKey(DiaDiem, related_name='madiadiemden', on_delete=models.CASCADE)
    ngaybatdau = models.DateTimeField()
    ngayketthuc = models.DateTimeField()
    trangthaitour = models.CharField(max_length=50) 
    imgTour = models.CharField(max_length=100)
    def __str__(self):
        return self.tentour


    

class LoaiTour(models.Model):
    maloaitour = models.CharField(max_length=5, primary_key=True)
    tenloaitour = models.CharField(max_length=50)
    tour = models.ManyToManyField(Tour, through='LoaiTour_Tour') 

class LoaiTour_Tour(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    loaitour = models.ForeignKey(LoaiTour, on_delete=models.CASCADE)
    giave = models.FloatField()

class PhuongTienDiChuyen(models.Model):
    maphuongtien = models.CharField(max_length=5, primary_key=True)
    tenphuongtien = models.CharField(max_length=50)
    socho = models.PositiveIntegerField()
    loaiphuongtien = models.CharField(max_length=50)
    matour = models.ForeignKey(Tour, on_delete=models.CASCADE)

class KhachHang(models.Model):
    makhachhang = models.CharField(max_length=5, primary_key=True)
    tenkhachhang = models.CharField(max_length=50)
    cmnd = models.PositiveIntegerField()
    ngaysinh = models.DateField()
    gioitinh = models.BooleanField()
    diachi = models.CharField(max_length=50)
    sodienthoai = models.PositiveIntegerField()
    tour = models.ManyToManyField(Tour, through='KhachHang_Tour')

class KhachHang_Tour(models.Model):
    matour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    makhachhang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    soluongvedat = models.PositiveIntegerField()
    thanhtien = models.FloatField()

class PhuLucKhachHang(models.Model):
    maphuluckhachhang = models.CharField(max_length=5, primary_key=True)
    tenphuluckhachhang = models.CharField(max_length=50)
    cmnd = models.PositiveIntegerField()
    ngaysinh = models.DateField()
    gioitinh = models.BooleanField()
    sodienthoai = models.PositiveIntegerField()
    makhachhang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)

class PhongBan(models.Model):
    maphongban = models.CharField(max_length=5, primary_key=True)
    tenphongban = models.CharField(max_length=50)

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

class TaiKhoan(models.Model):
    mataikhoan = models.CharField(max_length=5, primary_key=True)
    tentaikhoan = models.CharField(max_length=50)
    matkhau = models.CharField(max_length=50)
    manhanvien = models.ForeignKey(NhanVien, on_delete=models.CASCADE)

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

class HoaDon(models.Model):
    mahoadon = models.CharField(max_length=5, primary_key=True)
    ngaylaphoadon = models.DateField()
    giatrihoadon = models.FloatField()
    mahopdong = models.ForeignKey(HopDong, on_delete=models.CASCADE)