# -*- coding: utf8 -*-
from django.contrib import admin

# Register your models here.
# from .models import Tour
# admin.site.register(Tour)

# from .models import PhongBan
# admin.site.register(PhongBan)

# from .models import NhanVien
# admin.site.register(NhanVien)

from .models import HopDong

# class SearchHopDongAdmin(admin.ModelAdmin):
#     search_fields = ('title', 'author__name', 'comments__text', )

class SearchHopDongAdmin(admin.ModelAdmin):
    fields = ['mahopdong','ngayhethang', 'ngayki','giatrihopdong','noidunghopdong','manhanvien','makhachhang','matour'] 
    search_fields = ['mahopdong']

admin.site.register(HopDong, SearchHopDongAdmin)

