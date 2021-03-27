from django.urls import path
from . import views

urlpatterns = [
    path('', views.PhapCheDuoc, name='phap-che-duoc'),
    path('giao-trinh/', views.Level0ListView.as_view(), name='pcd-level0'),
    path('giao-trinh/<slug:slug>', views.Level0DetailView.as_view(), name='pcd-level0-detail'),
]
