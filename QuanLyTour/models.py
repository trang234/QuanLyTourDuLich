from django.db import models
from QuanLyNhanVien.models import NhanVien

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
	loaitour = models.ManyToManyField(LoaiTour, through='LoaiTour_Tour', on_delete=models.CASCADE)
	nhanvien = models.ManyToManyField(Tour, on_delete=models.CASCADE)

	trangthaitour_choices = (
		('CHUA_DI', 'Chưa đi'),
        ('DANG_DI', 'Đang đi'),
        ('DA_DI', 'Đã đi'),
		)
	trangthai = models.CharField(
        max_length=10,
        choices=trangthaitour_choices,
        default='CHUA_DI',
    )

	def  __str__(self):
		return self.tentour

class LoaiTour(models.Model):
	maloaitour_choices = (
		('TL000', 'TL000-LE'),
		('TD000', 'TD000-DOAN')
		)
	maloaitour = models.CharField(
		max_length=5, 
		primary_key=True,
		choices=maloaitour_choices,
		default='TL000'
		)

	tenloaitour = models.CharField(max_length=50)

	def __str__(self):
		return self.tenloaitour

class LoaiTour_Tour(models.Model):
	tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
	loaitour = models.ForeignKey(LoaiTour, on_delete=models.CASCADE)
	giave = models.FloatField()

class PhuongTienDiChuyen(models.Model):
	maphuongtien = models.CharField(max_length=5, primary_key=True)
	tenphuongtien = models.CharField(max_length=50)

	loaiphuongtien_choices = (
    	('XE_OTO', 'xeoto').
    	('TAU_HOA', 'Tauhoa'),
    	('MAY_BAY', 'Maybay'),
    	)
	loaiphuongtien = models.CharField(
		max_length=50,
		choices=loaiphuongtien_choices,
		default='XE_OTO',
		)

	socho_choices = (
		(7, 7),
        (16, 16),
        (32, 32),
        (50, 50)
		)
	socho = models.PositiveIntegerField(
        choices=socho_choices,
        default=50,
    )
	
	matour = models.ForeignKey(Tour, on_delete=models.CASCADE)