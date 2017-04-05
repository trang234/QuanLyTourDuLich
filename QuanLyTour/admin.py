from django.contrib import admin
from .models import DiaDiem, Tour, LoaiTour, PhuongTienDiChuyen, LoaiTour_Tour

# Register your models here.

# DiaDiem
class DiaDiemAdmin(admin.ModelAdmin):
    list_display = ('tendiadiem', 'mota')
    exclude = ['madiadiem']
    search_fields = ['tendiadiem']
    list_filter = ('tendiadiem',)
    ordering = ('-tendiadiem',)
admin.site.register(DiaDiem, DiaDiemAdmin)

# Tour
class TourAdmin(admin.ModelAdmin):
    list_display = ('tentour', 'madiadiemdi', 'madiadiemden', 'ngaybatdau', 'ngayketthuc', 'maphuongtien', 'imgpath')
    fields = ['matour', 'tentour', ('madiadiemdi', 'madiadiemden'), ('ngaybatdau', 'ngayketthuc'), 'nhanvien', 'maphuongtien', 'imgpath']
    search_fields = ['tentour', 'ngaybatdau', 'ngayketthuc', 'imgpath']
    list_filter = ('tentour', 'madiadiemdi', 'madiadiemden', 'loaitour', 
        'nhanvien', 'ngaybatdau', 'ngayketthuc', 'maphuongtien', 'imgpath')
    ordering = ('tentour', 'madiadiemdi', 'madiadiemden','loaitour', 
        'nhanvien', 'ngaybatdau', 'ngayketthuc', 'maphuongtien', 'imgpath')
admin.site.register(Tour, TourAdmin)

# LoaiTour
class LoaiTourAdmin(admin.ModelAdmin):
    list_display = ('tenloaitour',)
    exclude = ['maloaitour']
    search_fields = ['tenloaitour',]
    list_filter = ('tenloaitour',)
    ordering = ('tenloaitour',)
admin.site.register(LoaiTour, LoaiTourAdmin)

#PhuongTienDiChuyen
class PhuongTienDiChuyenAdmin(admin.ModelAdmin):
    list_display = ('tenphuongtien', 'loaiphuongtien', 'socho',)
    search_fields = ['tenphuongtien', 'loaiphuongtien', 'socho']
    list_filter = ('tenphuongtien', 'loaiphuongtien', 'socho',)
    ordering = ('tenphuongtien', 'loaiphuongtien', 'socho',)
admin.site.register(PhuongTienDiChuyen, PhuongTienDiChuyenAdmin)

#LoaiTour_Tour
class LoaiTour_TourAdmin(admin.ModelAdmin):
    list_display = ('tour', 'loaitour', 'giave',)
    search_fields = ['giave']
    list_filter = ('tour', 'loaitour', 'giave',)
    ordering = ('tour', 'loaitour', 'giave',)
admin.site.register(LoaiTour_Tour, LoaiTour_TourAdmin)