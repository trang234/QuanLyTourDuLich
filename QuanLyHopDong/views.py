from django.shortcuts import render

# Create your views here.
from QuanLyHopDong.models import HopDong

# def view(request, *args, **kwargs):
#     self = cls(**initkwargs)
#     if hasattr(self, 'get') and not hasattr(self, 'head'):
#         self.head = self.get
#     self.request = request
#     self.args = args
#     self.kwargs = kwargs
#     return self.dispatch(request, *args, **kwargs)


def index(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
    p = canvas.Canvas(response)

    def view(self, *args, **kwargs):
        hd = HopDong(models.Model)
        mahd =  getattr(hd, "mahopdong")
        p.drawString(100, 400, mahd)
        return self.dispatch(*args, **kwargs)

    
    p.showPage()
    p.save()
    return response