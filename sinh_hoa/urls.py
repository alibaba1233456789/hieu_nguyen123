from django.urls import path
from . import views

urlpatterns = [
    path('', views.SinhHoa, name='sinh-hoa'),
    path('giao-trinh/', views.Level0ListView.as_view(), name='sh-level0'),
    path('giao-trinh/<slug:slug>', views.Level0DetailView.as_view(), name='sh-level0-detail'),
]
