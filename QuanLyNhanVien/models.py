from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _


from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator

from django.http import HttpResponse, HttpResponseNotFound


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

    def clean(self):
        if len(self.maphongban) !=5:
            raise ValidationError(_('Mã phòng ban phải có 5 ký tự.'))

class NhanVien(models.Model):
    manhanvien = models.CharField(
        max_length=5, 
        primary_key=True, 
        verbose_name="Mã NV")

    tennhanvien = models.CharField(
        max_length=50, 
        verbose_name="Họ tên")

    # cmnd = models.BigIntegerField(
    #     verbose_name="CMND",
    #     validators=[MaxLengthValidator(12),MinLengthValidator(9)],
    #     unique=True)

    cmnd = models.CharField(
        verbose_name="CMND",
        max_length=12, 
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

    sodienthoai = models.CharField(
        verbose_name="SĐT",
        max_length=11)

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


    def clean(self):
        if len(self.cmnd) <= 8:
             raise ValidationError(_('CMND có 9 hoặc 12 ký tự.'))
        elif len(self.cmnd) >= 10 and len(self.cmnd) <= 11:
             raise ValidationError(_('CMND có 9 hoặc 12 ký tự.'))
      
        if len(self.sodienthoai) <= 9:
            raise ValidationError(_('SĐT phải có 10 hoặc 11 số'))

        if len(self.manhanvien)!=5:
            raise ValidationError(_('Mã nhân viên phải có 5 ký tự.'))
        

    # def save(self, *args, **kwargs):
    #     if self.sodienthoai < 1 or self.cmnd < 1:
    #         #self.erroreturn HttpResponse('<h1>Page was found</h1>')r_messages={'Error': 'Your custom error message'}
    #         print('Số điện thoại không âm hoặc CMND không âm.')
    #         #raise ValidationError('The pools are all full.')
    #     # elif self.tendiadiem == "Hà Nội":
    #     #     self.madiadiem = 'DD009'
    #     super(NhanVien, self).save(*args, **kwargs)


