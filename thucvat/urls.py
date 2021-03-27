"""thucvat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage


urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name = 'signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('duoc-lieu-hoc/', include('duoclieu.urls')),
    path('doc-chat-hoc/', include('doc_chat_hoc.urls')),
    path('duoc-lam-sang/', include('duoc_lam_sang.urls')),
    path('duoc-ly/', include('duoc_ly.urls')),
    path('hoa-duoc/', include('hoa_duoc.urls')),
    path('kiem-nghiem/', include('kiem_nghiem.urls')),
    path('cong-nghiep-duoc/', include('cong_nghiep_duoc.urls')),
    path('phap-che-duoc/', include('phap_che_duoc.urls')),
    path('hoa-ly/', include('hoa_ly.urls')),
    path('sinh-hoa/', include('sinh_hoa.urls')),
    path('cong-nghe-sinh-hoc/', include('cong_nghe_sinh_hoc.urls')),
    path('', RedirectView.as_view(url='home/', permanent=False)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
