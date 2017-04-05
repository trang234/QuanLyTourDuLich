from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _


from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



# Create your models here.

class PhongBan(models.Model):
    maphongban = models.CharField(
        max_length=5, 
        primary_key=True, 
        verbose_name="Mã PB")

    tenphongban = models.CharField(
        max_length=50, 
        verbose_name="Tên PB")
    def __str__(self):
        return self.maphongban + " " +self.tenphongban


class NhanVien(models.Model):
    manhanvien = models.CharField(
        max_length=5, 
        primary_key=True, 
        verbose_name="Mã NV")

    tennhanvien = models.CharField(
        max_length=50, 
        verbose_name="Họ tên")

    cmnd = models.PositiveIntegerField(
        verbose_name="CMND",
        unique=True)

    ngaysinh = models.DateField(verbose_name="Ngày sinh")

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

    sodienthoai = models.PositiveIntegerField(verbose_name="SĐT")

    CHUC_VU_CHOICE=(
        ('TRUONG_PHONG','Trưởng phòng'),
        ('PHO_PHONG','Phó phòng'),
        ('NHAN_VIEN_VAN_PHONG', 'Nhân viên văn phòng'),
        ('HUONG_DAN_VIEN', 'Hướng dẫn viên'),
        ('NHAN_VIEN_BAN_VE', 'Nhân viên bán vé')
    )
    chucvu = models.CharField(
        max_length=50, 
        choices=CHUC_VU_CHOICE, 
        default='NHAN_VIEN_VAN_PHONG',
        verbose_name="Chức vụ ")

    maphongban = models.ForeignKey(PhongBan, 
        on_delete=models.CASCADE, 
        verbose_name="Mã phòng ban")

    def get_sentinel_user():
        return get_user_model().objects.get_or_create(username='deleted')[0]

    tendangnhap = models.OneToOneField(settings.AUTH_USER_MODEL,
          on_delete=models.SET(get_sentinel_user),
          verbose_name="Tên đăng nhập")

    def __str__(self):
        return self.manhanvien + " " + self.tennhanvien


