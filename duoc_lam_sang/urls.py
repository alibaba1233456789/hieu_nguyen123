from django.urls import path
from . import views

urlpatterns = [
    path('', views.DuocLamSang, name='duoc-lam-sang'),
    path('giao-trinh/', views.Level0ListView.as_view(), name='dls-level0'),
    path('giao-trinh/<slug:slug>', views.Level0DetailView.as_view(), name='dls-level0-detail'),
]
