from django.contrib import admin
from .models import DiaDiem, Tour, LoaiTour, PhuongTienDiChuyen

# Register your models here.

# DiaDiem
admin.site.register(DiaDiem)

# Tour
admin.site.register(Tour)

# LoaiTour
admin.site.register(LoaiTour)

#PhuongTienDiChuyen
admin.site.register(PhuongTienDiChuyen)