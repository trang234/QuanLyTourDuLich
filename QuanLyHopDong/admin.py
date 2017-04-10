# -*- coding: utf8 -*-
from django.contrib import admin
from reportlab.pdfgen import canvas
from django.http import HttpResponse

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PyPDF2 import PdfFileWriter, PdfFileReader

from .models import HopDong
import tempfile
import zipfile

def print_Pdf(self, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
    p = canvas.Canvas(response)


    p.setLineWidth(.3)
    ttfFile = "/home/ngan-bui/ProjectThucTap/data/QuanLyTourDuLich/fonts/TimeNewRomanBold.ttf"
    pdfmetrics.registerFont(TTFont('TimeNewRomanBold', ttfFile))
    p.setFont('TimeNewRomanBold', 12)
    

    p.drawString(40,750,'CÔNG TY HAPPY TRAVEL')
    p.line(40,747,100,747)
    p.drawString(300,750, u"CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM")
    p.drawString(300,735, u'Độc Lập - Tự Do - Hạnh Phúc')
    p.line(300,732,450,732)
     
    p.drawString(200,700,'HỢP ĐỒNG')

     
    p.drawString(40,680,'Số: ..... /..... /HĐKT')

    p.drawString(40,668,"– Căn cứ Luật thương mại được Quốc hội nước Cộng hoà xã hội chủ nghĩa Việt Nam khóa XI, kỳ")
    p.drawString(40,655,"họp thứ VII thông qua ngày 14 tháng 06 năm 2005.") 
    p.drawString(40,640,"– Căn cứ Bộ luật dân sự được Quốc hội nước cộng hoà xã hội chủ nghĩa Việt Nam khoá XIII thông")
    p.drawString(40,625,"qua ngày 24 tháng 11 năm 2015.")
    p.drawString(40,610,"– Căn cứ nhu cầu và khả năng của hai bên.")
    p.drawString(40,595,"Hôm nay, ngày.....tháng....năm...., tại văn phòng Công Ty Happy Travel")
    p.drawString(40,580,"Chúng tôi gồm có:")
    p.drawString(40,565,"Bên A: CÔNG TY HAPPY TRAVEL")
    p.drawString(40,550,"Địa chỉ:.........................................................................................................................")
    p.drawString(40,535,"Người đại diện:.................................................................................................................")
    p.drawString(40,520,"Điện thoại:.............................................................. - Fax:...............................................")
    p.drawString(40,505,"Tài khoản:............................................................")
    p.drawString(40,490,"Tại:...........................................................................................................................")
    # # p.drawString(40,490, queryset.filter(mahopdong = (HopDong.objects.filter().first())))
    # print('Ma Hop Dong La%s' % queryset.filter(trangthaihopdong = "Đã ký"))
    p.drawString(40,470,"Bên B: CÔNG TY................................................................................................................")
    p.drawString(40,455,"Địa chỉ:.........................................................................................................................")
    p.drawString(40,440,"Người đại diện:.................................................................................................................")
    p.drawString(40,425,"Điện thoại:.............................................................. - Fax:...............................................")
    p.drawString(40,410,"Tài khoản:............................................................")
    p.drawString(40,395,"Tại:...........................................................................................................................")
    p.drawString(40,380,"Hai bên thống nhất ký một số điều khoản phục vụ khách du lịch như sau:")
    p.drawString(40,365,"ĐIỀU 1: CHƯƠNG TRÌNH THAM QUAN DU LỊCH")
    p.drawString(40,350,"Bên B tổ chức cho bên A chương trình:..........................................................................................")
    p.drawString(40,335,"(Có chương trình chi tiết và là một phần không thể tách rời của hợp đồng)")
    p.drawString(40,320,"ĐIỀU 2: SỐ LƯỢNG KHÁCH")
    p.drawString(40,305,"– Số lượng tối thiểu:...... người. (Gồm có:...... người lớn )")
    p.drawString(40,290,"Nếu bên A giảm quá số lượng khách tối thiểu như trên hợp đồng đã ký .... khách, bên A chịu 50%")
    p.drawString(40,275,"đơn giá mỗi khách giảm theo hợp đồng. Số lượng khách tăng được tính phát sinh theo đơn giá trên hợp đồng.")
    p.drawString(40,260,"ĐIỀU 3: THỜI GIAN THỰC HIỆN")
    p.drawString(40,245,"1. Thời gian thực hiện:...... ngày..... đêm, từ ngày .............. đến ngày..................................................")
    p.drawString(40,230,"2. Điểm đón: 01 điểm, cụ thể tại:........................................... ...................................................")
    p.drawString(40,215,"Đón khách: Vào lúc.............. ngày......... tháng......... năm.........")
    p.drawString(40,200,"3. Liên hệ trưởng đoàn: ...................................................... Tel:............................................")
    p.drawString(40,185,"Để đảm bảo tài sản và sự an toàn của Quý Khách,lái xe của công ty sẽ trả khách tại điểm mà xe đón khách lúc đầu.")
    p.drawString(40,170,"ĐIỀU 4: GIÁ TRỊ HỢP ĐỒNG")
    p.drawString(40,155,"Giá cho 01 khách:.................................... VNĐ. Tổng số khách theo hợp đồng: ....... người")
    p.drawString(40,140,"Tổng giá trị hợp đồng:......................................................... (................................ gồm 10% VAT):")
    p.drawString(40,125,"(Bằng Chữ: ..............................................................................................................)")
    p.drawString(40,110,"Bảo hiểm du lịch: Mức đền bù tối đa ............................đ/ người/ vụ. ")
    p.drawString(40,90,"ĐIỀU 5: THANH TOÁN")
    p.drawString(40,75,"1. Bên A tạm ứng cho bên B số tiền bằng 1/2 tổng hợp đồng:")
    p.drawString(40,60,"Lần 01: Bên A Tạm ứng cho bên B Số tiền:......................................................................................")
     
    p.showPage()
    p.save()
    return response

class SearchHopDongAdmin(admin.ModelAdmin):
    fields = ['mahopdong','ngayhethang', 'ngayki','giatrihopdong','noidunghopdong','manhanvien','makhachhang','matour'] 
    search_fields = ['mahopdong']
    list_display = ('mahopdong','trangthaihopdong')
    actions = [print_Pdf]
admin.site.register(HopDong, SearchHopDongAdmin)



