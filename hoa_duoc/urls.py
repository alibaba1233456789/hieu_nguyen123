from django.urls import path
from . import views

urlpatterns = [
    path('', views.HoaDuoc2, name='hoa-duoc'),
    path('giao-trinh/', views.Level0ListView.as_view(), name='hd-level0'),
    path('giao-trinh/<slug:slug>', views.Level0DetailView.as_view(), name='hd-level0-detail'),
]
