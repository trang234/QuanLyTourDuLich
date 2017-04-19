from django.db import models
from django.http import HttpResponse, HttpRequest
from QuanLyTour.models import Tour, DatTour
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


# Create your models here.
# Create: 19-03-2017

class KhachHang(models.Model):
    makhachhang = models.CharField(
        max_length=5, 
        primary_key=True,
        verbose_name="Mã KH ")

    tenkhachhang = models.CharField(
        max_length=50,
        verbose_name="Họ tên ")

    cmnd = models.CharField(
        verbose_name="CMND",
        max_length=12, 
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

    sodienthoai = models.CharField(
        verbose_name="SĐT",
        max_length=11)

    tour = models.ManyToManyField(Tour, 
        through='DatVe')

    def __str__(self):
        return self.makhachhang + " " + self.tenkhachhang

    def clean(self):
        if len(self.makhachhang)!=5:
            raise ValidationError(_('Mã khách hàng phải có 5 ký tự'))

        if len(self.cmnd) <= 8:
             raise ValidationError(_('CMND có 9 hoặc 12 ký tự.'))
        elif len(self.cmnd) >= 10 and len(self.cmnd) <= 11:
             raise ValidationError(_('CMND có 9 hoặc 12 ký tự.'))

        if len(self.sodienthoai) <= 9:
            raise ValidationError(_('SĐT phải có 10 hoặc 11 số'))


class PhuLucKhachHang(models.Model):
    maphuluckhachhang = models.CharField(
        max_length=5, 
        primary_key=True,
        verbose_name="Mã KHPL")

    tenphuluckhachhang = models.CharField(
        max_length=50,
        verbose_name="Tên KHPL")

    cmnd = models.CharField(
        verbose_name="CMND",
        max_length=12, 
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

    sodienthoai = models.CharField(
        verbose_name="SĐT",
        max_length=11)

    makhachhang = models.ForeignKey(KhachHang, 
        on_delete=models.CASCADE,
        verbose_name="Mã KHĐD")

    def __str__(self):
        return self.maphuluckhachhang + " " + self.tenphuluckhachhang

    def clean(self):
        if len(self.cmnd) <= 8:
             raise ValidationError(_('CMND có 9 hoặc 12 ký tự.'))
        elif len(self.cmnd) >= 10 and len(self.cmnd) <= 11:
             raise ValidationError(_('CMND có 9 hoặc 12 ký tự.'))

        if len(self.sodienthoai) <= 9:
            raise ValidationError(_('SĐT phải có 10 hoặc 11 số'))

        if len(self.maphuluckhachhang) != 5:
             raise ValidationError(_('Mã khách hàng phụ lục phải có 5 ký tự'))

class DatVe(models.Model):
    matour = models.ForeignKey(Tour, 
        on_delete=models.CASCADE,
        verbose_name="Mã Tour ")

    makhachhang = models.ForeignKey(KhachHang, 
        on_delete=models.CASCADE,
        verbose_name="Mã KH")

    # def sample_view(request):
    #   self.tennhanvien = request.user.username

    tennhanvien = models.CharField(
        max_length=50,
        verbose_name="Tên nhân viên "
        )

    soluongvecon = models.PositiveIntegerField(
        default = 0,
        verbose_name="Số lượng vé còn lại"
        )

    soluongvedadangky = models.PositiveIntegerField(
        default = 1,
        verbose_name="Số lượng vé đã đăng ký"
        )

    soluongvedat = models.PositiveIntegerField(
        default=0,
        verbose_name="Số lượng vé đặt")

    '''Get tour price'''
    # dè get_tour_price():
    #     #tour = DatVe._meta.get_field_by_name('matour')
    #     # giave = LoaiTour_Tour.objects.values_lít('giave', flat=True).get(tour="T0001")
    #     # soluongve = DatVe.objects.filter('soluongvedat')
    #     # soluongve = 3
    #     # soluongve = DatVe._meta.get_field('soluongvedat')
    #     # sotienphaitra = soluongve * giave

    #     #soluongve = DatVe._meta.get_field_by_name('soluongvedat')
    #     sotienphaitra = giave * self.soluongvedat

    #     return sotienphaitra

    # def get_thanh_tien():
    #   return 20;


    thanhtien = models.FloatField(
        verbose_name="Thành tiền"
        )

    def save(self, *args, **kwargs):
        '''giatien'''
        tentour = self.matour
        print(tentour)
        matour = Tour.objects.values_list('matour', flat=True).get(tentour=tentour)
        print(matour)
        giave = DatTour.objects.values_list('giave', flat=True).get(tour=self.matour)
        print(giave)
        self.thanhtien = self.soluongvedat * giave

        '''soluongvecon'''
        luongve = DatTour.objects.values_list('luongve', flat=True).get(tour=tentour)
        self.soluongvedadangky += self.soluongvedat
        self.soluongvecon = luongve - self.soluongvedadangky

        super(DatVe, self).save(*args, **kwargs)