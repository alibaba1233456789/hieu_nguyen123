from django.urls import path
from . import views

urlpatterns = [
    path('', views.HoaLy, name='hoa-ly'),
    path('giao-trinh/', views.Level0ListView.as_view(), name='hl-level0'),
    path('giao-trinh/<slug:slug>', views.Level0DetailView.as_view(), name='hl-level0-detail'),
]
