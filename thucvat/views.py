from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
#---------------------------------------------------
from duoclieu.models import HoThucVat, DuocLieu, Level0

def home(request):
    """View function for home page of site."""


    So_ho_thuc_vat = HoThucVat.objects.all().count()
    So_duoc_lieu = DuocLieu.objects.all().count()
    So_chuong = Level0.objects.all().count()

    context = {
        'So_ho_thuc_vat': So_ho_thuc_vat,
        'So_duoc_lieu': So_duoc_lieu,
        'So_chuong': So_chuong,
    }
    return render(request, 'home.html', context=context)
