from django.urls import path
from . import views

urlpatterns = [
    path('', views.CongNghiepDuoc, name='cong-nghiep-duoc'),
    path('giao-trinh/', views.Level0ListView.as_view(), name='cnd-level0'),
    path('giao-trinh/<slug:slug>', views.Level0DetailView.as_view(), name='cnd-level0-detail'),
]
