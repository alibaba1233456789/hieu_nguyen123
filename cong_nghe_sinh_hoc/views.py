from django.shortcuts import render
from django.views import generic

def CongNgheSinhHoc(request):
    return render(request, 'cong_nghe_sinh_hoc.html',)

#-----------------------------------------------------
from .models import  Level0, Level1, Level2, Level3, Level4, Level5

class Level0ListView (generic.ListView):
    model = Level0
#-----------------------------------------------------
class Level0DetailView(generic.DetailView):
    model = Level0
#-----------------------------------------------------
