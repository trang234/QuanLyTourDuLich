from django.db import models
from QuanLyNhanVien.models import NhanVien

# Create your models here.
class DiaDiem(models.Model):
	madiadiem = models.CharField(
		max_length=5, 
		primary_key=True, 
		verbose_name="Mã loại tour"
		)

	tendiadiem = models.CharField(
		max_length=50,
		verbose_name="Tên địa điểm"
		)

	mota = models.CharField(
		max_length=100,
		blank=True,
		verbose_name="Mô tả"
		)

	imgpath = models.CharField(
		max_length=50,
		verbose_name="Đường dẫn hình"
		)

	def __str__(self):
		return self.tendiadiem

class LoaiTour(models.Model):
	maloaitour_choices = (
		('TL000', 'TL000-LE'),
		('TD000', 'TD000-DOAN')
		)
	maloaitour = models.CharField(
		max_length=5, 
		primary_key=True,
		choices=maloaitour_choices,
		default='TL000',
		verbose_name="Mã loại tour"
		)

	def set_to_tenloaitour(self):
		if self.tenloaitour == 'TL000':
			self.tenloaitour = 'TOUR_LE'
		elif self.maloaitour == 'TD000':
			self.tenloaitour = 'TOUR_DOAN'
		return self.tenloaitour

	tenloaitour = models.CharField(
		max_length=50,
		verbose_name="Tên loại tour",
		default=property(set_to_tenloaitour)
		)

	def __str__(self):
		return self.tenloaitour

class PhuongTienDiChuyen(models.Model):
	maphuongtien = models.CharField(
		max_length=5, 
		primary_key=True,
		verbose_name="Mã phương tiện"
		)

	tenphuongtien_choices = (
		('Mercedes', 'Mercedes'),
		('Kia', 'Kia'),
		('Hyundai', 'Hyundai'),
		('Mitsubishi', 'Mitsubishi'),
		('Honda', 'Honda')
		)
	tenphuongtien = models.CharField(
		max_length=50,
		choices=tenphuongtien_choices,
		default='Mercedes',
		verbose_name="Tên phương tiện"
		)

	loaiphuongtien_choices = (
    	('XE_OTO', "Xe ô tô"),
    	)
	loaiphuongtien = models.CharField(
		max_length=50,
		choices=loaiphuongtien_choices,
		default='XE_OTO',
		verbose_name="Loại phương tiện"
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
        verbose_name="Số chỗ"
    )

	def  __str__(self):
		return self.tenphuongtien

class Tour(models.Model):
	matour = models.CharField(
		max_length=5, 
		primary_key=True,
		verbose_name="Mã tour"
		)

	tentour = models.CharField(
		max_length=50,
		verbose_name="Tên tour"
		)

	madiadiemdi = models.ForeignKey(
		DiaDiem,
		related_name='madiadiemdi', 
		null=True, 
		on_delete=models.CASCADE,
		verbose_name="Địa điểm đi"
		)

	madiadiemden = models.ForeignKey(
		DiaDiem, 
		related_name='madiadiemden', 
		null=True, 
		on_delete=models.CASCADE,
		verbose_name="Địa điểm đến"
		)

	ngaybatdau = models.DateTimeField(
		verbose_name="Ngày bắt đầu"
		)

	ngayketthuc = models.DateTimeField(
		verbose_name="Ngày kết thúc"
		)

	loaitour = models.ManyToManyField(
		LoaiTour, 
		through='LoaiTour_Tour',
		verbose_name="Loại tour"
		)

	nhanvien = models.ManyToManyField(
		NhanVien,
		verbose_name="Hướng dẫn viên"
		)

	trangthaitour_choices = (
		('CHUA_DI', "Chưa đi"),
        ('DANG_DI', "Đang đi"),
        ('DA_DI', "Đã đi"),
		)
	trangthai = models.CharField(
        max_length=10,
        choices=trangthaitour_choices,
        default='CHUA_DI',
        verbose_name="Trạng thái"
    )

	maphuongtien = models.ForeignKey(
		PhuongTienDiChuyen, 
		on_delete=models.CASCADE,
		verbose_name="Phương tiện"
		)

	def  __str__(self):
		return self.tentour

class LoaiTour_Tour(models.Model):
	tour = models.ForeignKey(
		Tour, 
		on_delete=models.CASCADE,
		verbose_name="Tour"
		)

	loaitour = models.ForeignKey(
		LoaiTour, 
		on_delete=models.CASCADE,
		verbose_name="Loại tour"
		)

	giave = models.FloatField(
		verbose_name="Gía vé"
		)