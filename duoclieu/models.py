from django.db import models
from django.urls import reverse
from datetime import date, datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

#------------------------------------------------------------------
class LoiNoiDauDL(models.Model):
    loi_noi_dau = models.TextField(max_length = 1000, verbose_name = 'Lời nói đầu', null = True, blank = True, help_text = 'Mỗi "+Add" là một đoạn trong lời nói đầu. Hãy nhập những lời tâm huyết của bạn vào đây vì đây là phần người đọc sẽ thấy đầu tiên khi chọn khối kiến thức dược liệu.')

    class Meta:
       verbose_name = 'Lời nói đầu'
       verbose_name_plural = '0. Lời nói đầu'
       ordering = ['id']

    def __str__(self):
        return f'Đoạn {self.id}'
#------------------------------------------------------------------

class HoThucVat(models.Model):
    La_tinh = models.CharField(max_length = 200, verbose_name ='họ latinh')
    Tieng_viet = models.CharField(max_length = 200, verbose_name = 'họ tiếng việt')
    ngay_dang = models.DateTimeField(auto_now=True, null=True, blank = True, verbose_name ='Ngày cập nhật')
    nguoi_dang = models.CharField(max_length = 200, null = True, blank = True, verbose_name ='người đăng', help_text = 'Tên tác giả, nếu không nhập thông tin chương trình sẽ mặc định là họ và tên của chủ tài khoản (thông tin khai báo lúc đăng ký tài khoản / tạo bởi admin).')
    gioi_thieu_chung = models.TextField(max_length = 1000, verbose_name = 'giới thiện chung', null = True, blank = True, help_text = 'Nếu không có gì để viết vào có thể để trống.')
    slug = models.SlugField(null=True, unique=True, help_text = 'Thông tin này sẽ hiển thị tại địa chỉ web, ví dụ: www.home/ho-thuc-vat/XXXXX, nếu không nhập dữ liệu chương trình sẽ mặc định XXXXX là họ dược liệu.')

    class Meta:
       verbose_name = 'Họ thực vật'
       verbose_name_plural = 'A. Họ thực vật'
       ordering = ['Tieng_viet']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.La_tinh)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.Tieng_viet} ({self.La_tinh})'

    def get_absolute_url(self):
        return reverse('hothucvat-detail', kwargs={'slug': self.slug})


#------------------------------------------------------------------
class DuocLieu(models.Model):
    ten_tieng_viet = models.CharField(max_length = 200, verbose_name ='Tên tiếng việt')
    ten_la_tinh = models.CharField(max_length = 200, verbose_name ='Tên Latinh')
    ho_thuc_vat = models.ForeignKey('HoThucVat', on_delete = models.CASCADE, verbose_name ='Họ thực vật',  help_text ='Kéo chọn họ thực vật phù hợp, nếu họ thực vật chưa có ấn vào dấu + để tạo mới.')
    ngay_dang = models.DateTimeField(auto_now=True, null=True, blank = True, verbose_name ='Ngày cập nhật')
    nguoi_dang = models.CharField(max_length = 200, null = True, blank = True, verbose_name ='người đăng', help_text = 'Tên tác giả, nếu không nhập thông tin chương trình sẽ mặc định là họ và tên của chủ tài khoản (thông tin khai báo lúc đăng ký tài khoản / tạo bởi admin).')
    slug = models.SlugField(null=True, blank=True, unique=True, help_text = 'Thông tin này sẽ hiển thị tại địa chỉ web, ví dụ: www.home/duoclieu/XXXXX, nếu không nhập dữ liệu chương trình sẽ mặc định XXXXX là tên khoa học của dược liệu.')

    class Meta:
        verbose_name = 'Dược liệu'
        verbose_name_plural = 'B. Dược liệu'
        ordering = ['ten_tieng_viet']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.ten_la_tinh)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.ten_tieng_viet} ({self.ten_la_tinh})'

    def get_absolute_url(self):
        return reverse('duoclieu-detail', kwargs={'slug': self.slug})
#------------------------------------------------------------------
class TenKhoaHoc(models.Model):
    duoc_lieu = models.ForeignKey('DuocLieu', on_delete = models.CASCADE, verbose_name = 'dược liệu')
    ten_tieng_viet_spp = models.CharField(max_length = 200, verbose_name = 'tên tiếng việt spp', null = True, blank = True)
    ten_latinh_spp = models.CharField(max_length = 200, verbose_name = 'tên latinh spp', null = True, blank = True)

    class Meta:
       verbose_name = 'tên khoa học spp'
       verbose_name_plural = 'tên khoa học spp'

class DacDiemVaPhanBo(models.Model):
    duoc_lieu = models.ForeignKey('DuocLieu', on_delete = models.CASCADE, verbose_name = 'dược liệu')
    dac_diem_va_phan_bo = models.TextField(max_length = 1000, verbose_name = 'đặc điểm và phân bố')

    class Meta:
       verbose_name = 'đặc điểm và phân bố'
       verbose_name_plural = 'đặc điểm và phân bố'

class BoPhanDung(models.Model):
    duoc_lieu = models.ForeignKey('DuocLieu', on_delete = models.CASCADE, verbose_name = 'dược liệu')
    bo_phan_dung = models.TextField(max_length = 1000, verbose_name = 'bộ phận dùng')

    class Meta:
       verbose_name = 'bộ phận dùng'
       verbose_name_plural = 'bộ phận dùng'

class DacDiemViPhauVaBot(models.Model):
    duoc_lieu = models.ForeignKey('DuocLieu', on_delete = models.CASCADE, verbose_name = 'dược liệu')
    dac_diem_vi_phau_va_bot = models.TextField(max_length = 1000, verbose_name = 'đặc điểm vi phẫu và bột')

    class Meta:
       verbose_name = 'đặc điểm vi phẫu và bột'
       verbose_name_plural = 'đặc điểm vi phẫu và bột'

class TacDungVaCongDung(models.Model):
    duoc_lieu = models.ForeignKey('DuocLieu', on_delete = models.CASCADE, verbose_name = 'dược liệu')
    tac_dung_va_cong_dung = models.TextField(max_length = 1000, verbose_name = 'tác dụng và công dụng')

    class Meta:
       verbose_name = 'tác dụng và công dụng'
       verbose_name_plural = 'tác dụng và công dụng'

class CheBien(models.Model):
    duoc_lieu = models.ForeignKey('DuocLieu', on_delete = models.CASCADE, verbose_name = 'dược liệu')
    che_bien = models.TextField(max_length = 1000, verbose_name = 'chế biến')

    class Meta:
       verbose_name = 'chế biến'
       verbose_name_plural = 'chế biến'

class ChePham(models.Model):
    duoc_lieu = models.ForeignKey('DuocLieu', on_delete = models.CASCADE, verbose_name = 'dược liệu')
    che_pham = models.TextField(max_length = 1000, verbose_name = 'chế phẩm')

    class Meta:
       verbose_name = 'chế phẩm'
       verbose_name_plural = 'chế phẩm'

class ChuY(models.Model):
    duoc_lieu = models.ForeignKey('DuocLieu', on_delete = models.CASCADE, verbose_name = 'dược liệu')
    chu_y = models.TextField(max_length = 1000, verbose_name = 'chú ý')

    class Meta:
       verbose_name = 'chú ý'
       verbose_name_plural = 'chú ý'

class GhiChu(models.Model):
    duoc_lieu = models.ForeignKey('DuocLieu', on_delete = models.CASCADE, verbose_name = 'dược liệu')
    ghi_chu = models.TextField(max_length = 1000, verbose_name = 'ghi chú')

    class Meta:
       verbose_name = 'ghi chú'
       verbose_name_plural = 'ghi chú'

class HinhAnhMinhHoa(models.Model):
    duoc_lieu = models.ForeignKey('DuocLieu', on_delete = models.CASCADE, verbose_name = 'dược liệu')
    hinh_anh_minh_hoa = models.ImageField(upload_to='duoclieu', verbose_name = 'hình ảnh minh hoạ')

    class Meta:
       verbose_name = 'hình ảnh minh hoạ'
       verbose_name_plural = 'hình ảnh minh hoạ'

class HinhAnhBoSung(models.Model):
    duoc_lieu = models.ForeignKey('DuocLieu', on_delete = models.CASCADE, verbose_name = 'dược liệu')
    hinh_anh_bo_sung = models.ImageField(upload_to='duoclieu', verbose_name = 'hình ảnh bổ sung')

    class Meta:
       verbose_name = 'hình ảnh bổ sung'
       verbose_name_plural = 'hình ảnh bổ sung'

class ThanhPhanHoaHoc(models.Model):
    duoc_lieu = models.ForeignKey('DuocLieu', on_delete = models.CASCADE, verbose_name = 'dược liệu')
    thanh_phan_hoa_hoc = models.TextField(max_length = 1000, verbose_name = 'thành phần hoá học')

    class Meta:
       verbose_name = 'thành phần hoá học'
       verbose_name_plural = 'thành phần hoá học'

#------------------------------------------------------------------
#------------------------------------------------------------------
class Level0(models.Model):
    tieu_de_chinh = models.CharField(max_length = 200, verbose_name = 'tiêu đề chính')
    noi_dung = models.TextField(max_length = 3000, verbose_name = 'mục tiêu', null=True, blank = True)
    nguoi_dang = models.CharField(max_length = 200, null = True, blank = True, verbose_name ='người đăng', help_text = 'Tên tác giả, nếu không nhập thông tin chương trình sẽ mặc định là họ và tên của chủ tài khoản (thông tin khai báo lúc đăng ký tài khoản / tạo bởi admin).')
    slug = models.SlugField(null=True, unique=True, allow_unicode =True, help_text = 'Thông tin này sẽ hiển thị tại địa chỉ web, ví dụ: www.home/duoclieu/XXXXX, với XXXX là thông tin bạn nhập vào')

    def __str__(self):
        return f'{self.tieu_de_chinh}'

    def get_absolute_url(self):
        return reverse('level0-detail', kwargs={'slug': self.slug})

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
    noi_dung = models.TextField(max_length = 3000, verbose_name = 'nội dung', null=True, blank = True)
    level_0 = models.ForeignKey('Level0', on_delete = models.CASCADE, verbose_name = '<-- Tiêu đề chính')
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
    noi_dung = models.TextField(max_length = 3000, verbose_name = 'nội dung', null=True, blank = True)
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
    noi_dung = models.TextField(max_length = 3000, verbose_name = 'nội dung', null=True, blank = True)
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
    noi_dung = models.TextField(max_length = 3000, verbose_name = 'nội dung', null=True, blank = True)
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
    noi_dung = models.TextField(max_length = 3000, verbose_name = 'nội dung', null=True, blank = True)
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
