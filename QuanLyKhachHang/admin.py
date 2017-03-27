from django.contrib import admin
from .models import KhachHang,PhuLucKhachHang, DatVe
# Register your models here.

class KhachHangAdmin(admin.ModelAdmin):
	list_display = (
		'makhachhang','tenkhachhang', 'cmnd', 'ngaysinh',
		'gioitinh', 'diachi', 'sodienthoai')
	search_fields = ['makhachhang','tenkhachhang']
admin.site.register(KhachHang, KhachHangAdmin)

class PhuLucKhachHangAdmin(admin.ModelAdmin):
	list_display = (
		'maphuluckhachhang','tenphuluckhachhang', 'cmnd', 'ngaysinh',
		'gioitinh', 'sodienthoai', 'makhachhang')
admin.site.register(PhuLucKhachHang, PhuLucKhachHangAdmin)

class DatVeAdmin(admin.ModelAdmin):
	list_display = (
		'matour','makhachhang', 'tennhanvien', 'soluongvedat', 'thanhtien')
	readonly_fields = ["thanhtien"]
admin.site.register(DatVe, DatVeAdmin)
