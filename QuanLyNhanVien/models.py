from django.db import models

# Create your models here.

class PhongBan(models.Model):
	maphongban = models.CharField(max_length=5, primary_key=True)
	tenphongban = models.CharField(max_length=50)
	def __str__(self):
		return self.maphongban + " " +self.tenphongban


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
		return self.manhanvien + " " + self.tennhanvien
