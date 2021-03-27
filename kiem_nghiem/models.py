from django.db import models
from django.urls import reverse
from datetime import date, datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
#------------------------
class Level0(models.Model):
    tieu_de_chinh = models.CharField(max_length = 200, verbose_name = 'tiêu đề chính')
    noi_dung = models.TextField(max_length = 2000, verbose_name = 'mục tiêu', null=True, blank = True)
    nguoi_dang = models.CharField(max_length = 200, null = True, blank = True, verbose_name ='người đăng', help_text = 'Tên tác giả, nếu không nhập thông tin chương trình sẽ mặc định là họ và tên của chủ tài khoản (thông tin khai báo lúc đăng ký tài khoản / tạo bởi admin).')
    slug = models.SlugField(null=True, unique=True, allow_unicode =True, help_text = 'Thông tin này sẽ hiển thị tại địa chỉ web, ví dụ: www.home/duoclieu/XXXXX, với XXXX là thông tin bạn nhập vào')

    def __str__(self):
        return f'{self.tieu_de_chinh}'

    def get_absolute_url(self):
        return reverse('kn-level0-detail', kwargs={'slug': self.slug})

    class Meta:
       verbose_name = 'Tiêu để chính'
       verbose_name_plural = 'C. Tiêu để chính'
       ordering = ['id']
#---------------------
class HinhAnhLv0(models.Model):
    level_0 = models.ForeignKey('Level0', on_delete = models.CASCADE)
    hinh = models.ImageField(upload_to='giaotrinh')
    ten_hinh = models.CharField(max_length = 200)
#---------------------
class Level1(models.Model):
    tieu_de_1 = models.CharField(max_length = 200, verbose_name = 'tiêu đề cấp 1', null=True, blank = True)
    noi_dung = models.TextField(max_length = 2000, verbose_name = 'nội dung', null=True, blank = True)
    level_0 = models.ForeignKey('Level0', on_delete = models.CASCADE, verbose_name = '<-- Level0')

    def __str__(self):
        return f'{self.tieu_de_1}:'

    class Meta:
       verbose_name = 'Tiêu đề cấp 1'
       verbose_name_plural = 'C.1 - Tiêu đề cấp 1'
       ordering = ['id']
#---------------------
class HinhAnhLv1(models.Model):
    level_1 = models.ForeignKey('Level1', on_delete = models.CASCADE)
    hinh = models.ImageField(upload_to='giaotrinh')
    ten_hinh = models.CharField(max_length = 200)
#---------------------
class Level2(models.Model):
    tieu_de_2 = models.CharField(max_length = 200, verbose_name = 'tiêu đề cấp 2', null=True, blank = True)
    noi_dung = models.TextField(max_length = 2000, verbose_name = 'nội dung', null=True, blank = True)
    level_1 = models.ForeignKey('Level1', on_delete = models.CASCADE, verbose_name = '<-- Tiêu đề cấp 1')

    def __str__(self):
        return f'{self.tieu_de_2}:'

    class Meta:
       verbose_name = 'Tiêu đề cấp 2'
       verbose_name_plural = 'C.1.1 - Tiêu đề cấp 2'
       ordering = ['id']
#---------------------
class HinhAnhLv2(models.Model):
    level_2 = models.ForeignKey('Level2', on_delete = models.CASCADE)
    hinh = models.ImageField(upload_to='giaotrinh')
    ten_hinh = models.CharField(max_length = 200)
#---------------------
class Level3(models.Model):
    tieu_de_3 = models.CharField(max_length = 200, verbose_name = 'tiêu đề cấp 3', null=True, blank = True)
    noi_dung = models.TextField(max_length = 2000, verbose_name = 'nội dung', null=True, blank = True)
    level_2 = models.ForeignKey('Level2', on_delete = models.CASCADE, verbose_name = '<-- Tiêu đề cấp 2')

    def __str__(self):
        return f'{self.tieu_de_3}:'

    class Meta:
       verbose_name = 'Tiêu đề cấp 3'
       verbose_name_plural = 'C.1.1.1 - Tiêu đề cấp 3'
       ordering = ['id']
#---------------------
class HinhAnhLv3(models.Model):
    level_3 = models.ForeignKey('Level3', on_delete = models.CASCADE)
    hinh = models.ImageField(upload_to='giaotrinh')
    ten_hinh = models.CharField(max_length = 200)
#---------------------
class Level4(models.Model):
    tieu_de_4 = models.CharField(max_length = 200, verbose_name = 'tiêu đề cấp 4', null=True, blank = True)
    noi_dung = models.TextField(max_length = 2000, verbose_name = 'nội dung', null=True, blank = True)
    level_3 = models.ForeignKey('Level3', on_delete = models.CASCADE, verbose_name = '<-- Tiêu đề cấp 3')

    def __str__(self):
        return f'{self.tieu_de_4}:'

    class Meta:
       verbose_name = 'Tiêu đề cấp 4'
       verbose_name_plural = 'C.1.1.1.1 - Tiêu đề cấp 4'
       ordering = ['id']
#---------------------
class HinhAnhLv4(models.Model):
    level_4 = models.ForeignKey('Level4', on_delete = models.CASCADE)
    hinh = models.ImageField(upload_to='giaotrinh')
    ten_hinh = models.CharField(max_length = 200)
#---------------------
class Level5(models.Model):
    tieu_de_5 = models.CharField(max_length = 200, verbose_name = 'tiêu đề cấp 5', null=True, blank = True)
    noi_dung = models.TextField(max_length = 2000, verbose_name = 'nội dung', null=True, blank = True)
    level_4 = models.ForeignKey('Level4', on_delete = models.CASCADE, verbose_name = '<-- Tiêu đề cấp 4')

    def __str__(self):
        return f'{self.tieu_de_5}:'

    class Meta:
       verbose_name = 'Tiêu đề cấp 5'
       verbose_name_plural = 'C.1.1.1.1.1 - Tiêu đề cấp 5'
       ordering = ['id']
#---------------------
class HinhAnhLv5(models.Model):
    level_5 = models.ForeignKey('Level5', on_delete = models.CASCADE)
    hinh = models.ImageField(upload_to='giaotrinh')
    ten_hinh = models.CharField(max_length = 200)
#---------------------
