from django.urls import path
from . import views

urlpatterns = [
    path('', views.DuocLy, name='duoc-ly'),
    path('giao-trinh/', views.Level0ListView.as_view(), name='dl-level0'),
    path('giao-trinh/<slug:slug>', views.Level0DetailView.as_view(), name='dl-level0-detail'),
]
