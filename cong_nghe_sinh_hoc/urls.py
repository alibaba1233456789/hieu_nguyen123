from django.urls import path
from . import views

urlpatterns = [
    path('', views.CongNgheSinhHoc, name='cong-nghe-sinh-hoc'),
    path('giao-trinh/', views.Level0ListView.as_view(), name='cnsh-level0'),
    path('giao-trinh/<slug:slug>', views.Level0DetailView.as_view(), name='cnsh-level0-detail'),
]
