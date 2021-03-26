from django.urls import path
from . import views

urlpatterns = [
    path('', views.DuocLieuHoc, name='duoc-lieu-hoc'),
    path('ho-thuc-vat/', views.HoThucVatListView. as_view(), name='ho-thuc-vat'),
    path('ho-thuc-vat/<slug:slug>', views.HoThucVatDetailView.as_view(), name='hothucvat-detail'),
    path('duoc-lieu/', views.DuocLieuListView.as_view(), name='duoclieu'),
    path('duoc-lieu/<slug:slug>', views.DuocLieuDetailView.as_view(), name='duoclieu-detail'),
    path('giao-trinh/', views.Level0ListView.as_view(), name='level0'),
    path('giao-trinh/<slug:slug>', views.Level0DetailView.as_view(), name='level0-detail'),
]
