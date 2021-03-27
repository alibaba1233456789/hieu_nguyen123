from django.urls import path
from . import views

urlpatterns = [
    path('', views.KiemNghiem, name='kiem-nghiem'),
    path('giao-trinh/', views.Level0ListView.as_view(), name='kn-level0'),
    path('giao-trinh/<slug:slug>', views.Level0DetailView.as_view(), name='kn-level0-detail'),
]
