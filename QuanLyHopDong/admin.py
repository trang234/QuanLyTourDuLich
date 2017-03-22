from django.contrib import admin

# Register your models here.
from .models import Tour
admin.site.register(Tour)
from .models import PhongBan
admin.site.register(PhongBan)
from .models import NhanVien
admin.site.register(NhanVien)
from .models import HopDong
admin.site.register(HopDong)
