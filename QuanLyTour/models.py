from django.db import models
from QuanLyNhanVien import NhanVien

# Create your models here.
class DiaDiem(models.Model):
	madiadiem = models.CharField(max_length=5, primary_key=True)
	tendiadiem = models.CharField(max_length=50)
	mota = models.CharField(max_length=100)
	imgpath = models.CharField(max_length=50)

	def __str__(self):
		return self.tendiadiem

class Tour(models.Model):
	matour = models.CharField(max_length=5, primary_key=True)
	tentour = models.CharField(max_length=50)
	madiadiemdi = models.ForeignKey(DiaDiem, related_name='madiadiemdi', null=True, on_delete=models.CASCADE)
	madiadiemden = models.ForeignKey(DiaDiem, related_name='madiadiemden', null=True, on_delete=models.CASCADE)
	ngaybatdau = models.DateTimeField()
	ngayketthuc = models.DateTimeField()
	nhanvien = models.ManyToManyField(Tour, on_delete=models.CASCADE)

	trangthaitour_choice = (
		('CHUA_DI', 'Chưa đi'),
        ('DANG_DI', 'Đang đi'),
        ('DA_DI', 'Đã đi'),
		)
	trangthai = models.CharField(
        max_length=10,
        choices=trangthaitour_choice,
        default='CHUA_DI',
    )

	def  __str__(self):
		return self.tentour

class LoaiTour(models.Model):
	maloaitour = models.CharField(max_length=5, primary_key=True)
	tenloaitour = models.CharField(max_length=50)
	tour = models.ManyToManyField(Tour, through='LoaiTour_Tour')

	def __str__(self):
		return self.tenloaitour

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