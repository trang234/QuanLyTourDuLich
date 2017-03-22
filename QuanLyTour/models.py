from django.db import models
from QuanLyNhanVien.models import NhanVien

# Create your models here.
class DiaDiem(models.Model):
	madiadiem = models.CharField(
		max_length=5, 
		primary_key=True
		)

	tendiadiem_choices = (
		("Thành phố Hồ Chí Minh", "Thành phố Hồ Chí Minh"),
		("Nha Trang", "Nha Trang"),
		("Vũng Tàu", "Vũng Tàu"),
		("Phan Thiết", "Phan Thiết"),
		("Vịnh Hạ Long", "Vịnh Hạ Long"),
		("Cố Đô Huế", "Cố Đô Huế"),
		("Phố Cổ Hội An", "Phố Cổ Hội An"),
		("Đà Nẵng", "Đà Nẵng"),
		("Hà Nội", "Hà Nội")
		)
	tendiadiem = models.CharField(
		max_length=50,
		choices=tendiadiem_choices,
		default="Thành phố Hồ Chí Minh",
		verbose_name="Địa điểm"
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

	def save(self, *args, **kwargs):
		if self.tendiadiem == "Thành phố Hồ Chí Minh":
			self.madiadiem = 'DD001'
		elif self.tendiadiem == "Nha Trang":
			self.madiadiem = 'DD002'
		elif self.tendiadiem == "Vũng Tàu":
			self.madiadiem = 'DD003'
		elif self.tendiadiem == "Phan Thiết":
			self.madiadiem = 'DD004'
		elif self.tendiadiem == "Vịnh Hạ Long":
			self.madiadiem = 'DD005'
		elif self.tendiadiem == "Cố Đô Huế":
			self.madiadiem = 'DD006'
		elif self.tendiadiem == "Phố Cổ Hội An":
			self.madiadiem = 'DD007'
		elif self.tendiadiem == "Đà Nẵng":
			self.madiadiem = 'DD008'
		elif self.tendiadiem == "Hà Nội":
			self.madiadiem = 'DD009'
		super(DiaDiem, self).save(*args, **kwargs)

class LoaiTour(models.Model):
	maloaitour = models.CharField(
		max_length=5, 
		primary_key=True,
		verbose_name="Mã loại tour"
		) 
	
	tenloaitour_choices = (
		("Tour lẻ", "Tour lẻ"),
		("Tour đoàn", "Tour đoàn")
		)
	tenloaitour = models.CharField(
		max_length=50,
		choices=tenloaitour_choices,
		default="Tour lẻ",
		verbose_name="Loại tour"
		)

	def save(self, *args, **kwargs):
		if self.tenloaitour == "Tour lẻ":
			self.maloaitour = 'TL000'
		elif self.tenloaitour == "Tour đoàn":
			self.maloaitour = 'TD000'
		super(LoaiTour, self).save(*args, **kwargs)

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
    	("Xe ô tô", "Xe ô tô"),
    	)
	loaiphuongtien = models.CharField(
		max_length=50,
		choices=loaiphuongtien_choices,
		default="Xe ô tô",
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
		("Chưa đi", "Chưa đi"),
        ("Đang đi", "Đang đi"),
        ("Đã đi", "Đã đi"),
		)
	trangthai = models.CharField(
        max_length=10,
        choices=trangthaitour_choices,
        default="Chưa đi",
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