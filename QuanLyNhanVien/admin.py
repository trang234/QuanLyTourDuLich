from django.contrib import admin

# Register your models here.
from .models import PhongBan
from .models import NhanVien

admin.site.register(PhongBan)
admin.site.register(NhanVien)