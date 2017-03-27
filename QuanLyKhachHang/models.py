from django.db import models
from django.http import HttpResponse
from QuanLyTour.models import Tour, LoaiTour_Tour

# Create your models here.
# Create: 19-03-2017

class KhachHang(models.Model):
	makhachhang = models.CharField(
		max_length=5, 
		primary_key=True,
		verbose_name="Mã khách hàng ")

	tenkhachhang = models.CharField(
		max_length=50,
		verbose_name="Tên khách hàng ")

	cmnd = models.PositiveIntegerField(
		verbose_name="CMND ",
		unique=True)

	ngaysinh = models.DateField(
		verbose_name="Ngày sinh ")

	GIOI_TINH_CHOICE=(
		(True,'Nam'),
		(False,'Nữ')
		)
	gioitinh = models.BooleanField(
		verbose_name="Giới tính", 
		choices=GIOI_TINH_CHOICE,
		default=True)

	diachi = models.CharField(
		max_length=50,
		verbose_name="Địa chỉ ")

	sodienthoai = models.PositiveIntegerField(
		verbose_name="SĐT ")

	tour = models.ManyToManyField(Tour, 
		through='DatVe')

	def __str__(self):
		return self.makhachhang + " " + self.tenkhachhang

class PhuLucKhachHang(models.Model):
	maphuluckhachhang = models.CharField(
		max_length=5, 
		primary_key=True,
		verbose_name="Mã khách hàng PL")

	tenphuluckhachhang = models.CharField(
		max_length=50,
		verbose_name="Tên khách hàng PL")

	cmnd = models.PositiveIntegerField(
		verbose_name="CMND ",
		unique=True)

	ngaysinh = models.DateField(
		verbose_name="Ngày sinh ")

	GIOI_TINH_CHOICE=(
		(True,'Nam'),
		(False,'Nữ')
		)
	gioitinh = models.BooleanField(
		verbose_name="Giới tính", 
		choices=GIOI_TINH_CHOICE,
		default=True)

	sodienthoai = models.PositiveIntegerField(
		verbose_name="SĐT")

	makhachhang = models.ForeignKey(KhachHang, 
		on_delete=models.CASCADE,
		verbose_name="Mã khách hàng đại diện")

	def __str__(self):
		return self.maphuluckhachhang + " " + self.tenphuluckhachhang

class DatVe(models.Model):
	matour = models.ForeignKey(Tour, 
		on_delete=models.CASCADE,
		verbose_name="Mã Tour ")

	makhachhang = models.ForeignKey(KhachHang, 
		on_delete=models.CASCADE,
		verbose_name="Mã khách hàng ")

	tennhanvien = models.CharField(
		max_length=50,
		verbose_name="Tên nhân viên ")

	soluongvedat = models.PositiveIntegerField(
		default=0,
		verbose_name="Số lượng vé ")

	'''Get tour price'''
	def get_tour_price():
		# tour = DatVe._meta.get_field('matour')
		giave = LoaiTour_Tour.objects.values_list('giave', flat=True).get(tour="T0001")
		# soluongve = DatVe.objects.filter('soluongvedat')
		soluongve = 2
		sotienphaitra = soluongve * giave
		return sotienphaitra

	# def get_thanh_tien():
	# 	return 20;


	thanhtien = models.FloatField(
		# default=property(get_tour_price),
		# default=0,
		default=get_tour_price,
		verbose_name="Thành tiền")

	def sample_view(request):
		self.tennhanvien = request.user

	def __str__(self):
		return (self.thanhtien, self.get_gender_display())