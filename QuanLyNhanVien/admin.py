from django.contrib import admin


# Register your models here.
from .models import PhongBan, NhanVien

class PhongBanAdmin(admin.ModelAdmin):
	list_display = (
		'maphongban','tenphongban')
admin.site.register(PhongBan, PhongBanAdmin)


class NhanVienAdmin(admin.ModelAdmin):
	list_display = (
		'manhanvien','tennhanvien','cmnd', 'ngaysinh',
		'gioitinh', 'diachi', 'sodienthoai', 'chucvu', 'tendangnhap','maphongban')
admin.site.register(NhanVien, NhanVienAdmin)
