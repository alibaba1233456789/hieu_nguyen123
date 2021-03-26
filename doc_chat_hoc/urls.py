from django.urls import path
from . import views

urlpatterns = [
    path('', views.DocChatHoc, name='doc-chat-hoc'),
    path('giao-trinh/', views.Level0ListView.as_view(), name='dch-level0'),
    path('giao-trinh/<slug:slug>', views.Level0DetailView.as_view(), name='dch-level0-detail'),
]
