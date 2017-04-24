from django.contrib import admin
from .models import KhachHang,PhuLucKhachHang, DatVe
from import_export import resources
from import_export.admin import ImportExportMixin
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class KhachHangAdmin(admin.ModelAdmin):
    list_display = (
        'makhachhang','tenkhachhang', 'cmnd', 'ngaysinh',
        'gioitinh', 'diachi', 'sodienthoai')
    search_fields = ['makhachhang','tenkhachhang', 'cmnd', 'sodienthoai']
admin.site.register(KhachHang, KhachHangAdmin)

class PhuLucKhachHangResource(resources.ModelResource):

    class Meta:
        model = PhuLucKhachHang
     
       
class PhuLucKhachHangAdmin(ImportExportModelAdmin):
    list_display = (
        'maphuluckhachhang','tenphuluckhachhang', 'cmnd', 'ngaysinh',
        'gioitinh', 'sodienthoai', 'makhachhang')
    search_fields = ['maphuluckhachhang','tenphuluckhachhang','cmnd', 'sodienthoai']
    resource_class = PhuLucKhachHangResource
    pass
admin.site.register(PhuLucKhachHang, PhuLucKhachHangAdmin)

class DatVeAdmin(admin.ModelAdmin):
    list_display = (
        'matour','makhachhang', 'tennhanvien', 'soluongvecon', 
        'soluongvedadangky', 'soluongvedat', 'thanhtien')
    readonly_fields = ["thanhtien"]
admin.site.register(DatVe, DatVeAdmin)
