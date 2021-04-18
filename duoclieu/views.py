from django.shortcuts import render
from .models import LoinoiDauDL, HoThucVat, DuocLieu, Level0
#-----------------------------------------------------
def DuocLieuHoc(request):
    """View function for home page of site."""

    So_ho_thuc_vat = HoThucVat.objects.all().count()
    So_duoc_lieu = DuocLieu.objects.all().count()
    So_chuong = Level0.objects.all().count()
    Loi_noi_dau = LoinoiDauDL.objects.all()

    context = {
        'So_ho_thuc_vat': So_ho_thuc_vat,
        'So_duoc_lieu': So_duoc_lieu,
        'So_chuong': So_chuong,
        'Loi_noi_dau': Loi_noi_dau
    }
    return render(request, 'duoc_lieu_hoc.html', context=context)

#-----------------------------------------------------
from django.views import generic

class HoThucVatListView (generic.ListView):
    model = HoThucVat
#-----------------------------------------------------
class HoThucVatDetailView(generic.DetailView):
    model = HoThucVat
#-----------------------------------------------------
class DuocLieuListView (generic.ListView):
    model = DuocLieu
#-----------------------------------------------------
from django.contrib.auth.mixins import LoginRequiredMixin

class DuocLieuDetailView(LoginRequiredMixin, generic.DetailView):
    model = DuocLieu
#-----------------------------------------------------
from .models import  Level0, Level1, Level2, Level3, Level4, Level5

class Level0ListView (generic.ListView):
    model = Level0
#-----------------------------------------------------
class Level0DetailView(generic.DetailView):
    model = Level0
#-----------------------------------------------------

#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
