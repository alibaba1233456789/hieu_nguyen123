from django.contrib import admin
from .models import LoinoiDauDL, HoThucVat, DuocLieu, DacDiemVaPhanBo, BoPhanDung, DacDiemViPhauVaBot, ThanhPhanHoaHoc, TacDungVaCongDung, CheBien, HinhAnhMinhHoa, ChePham, ChuY, GhiChu, HinhAnhBoSung, TenKhoaHoc
#--------------------------------------
admin.site.register(LoinoiDauDL)
#--------------------------------------
class DuocLieuInline(admin.TabularInline):
    model = DuocLieu
    extra = 0


@admin.register(HoThucVat)
class HoThucVatAdmin(admin.ModelAdmin):
    list_display =('Tieng_viet', 'La_tinh', 'ngay_dang','nguoi_dang')
    inlines = [DuocLieuInline]
    prepopulated_fields = {'slug': ('La_tinh',)}

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'nguoi_dang', None) is None:
            obj.nguoi_dang = request.user.last_name +" "+ request.user.first_name
        obj.save()
#--------------------------------------
class TenKhoaHocInline(admin.TabularInline):
    model = TenKhoaHoc
    extra = 0

class HinhAnhBoSungInline(admin.TabularInline):
    model = HinhAnhBoSung
    extra = 0

class GhiChuInline(admin.TabularInline):
    model = GhiChu
    extra = 0

class ChuYInline(admin.TabularInline):
    model = ChuY
    extra = 0

class ChePhamInline(admin.TabularInline):
    model = ChePham
    extra = 0

class DacDiemVaPhanBoInline(admin.TabularInline):
    model = DacDiemVaPhanBo
    extra = 0

class BoPhanDungInline(admin.TabularInline):
    model = BoPhanDung
    extra = 0

class ThanhPhanHoaHocInline(admin.TabularInline):
    model = ThanhPhanHoaHoc
    extra = 0

class DacDiemViPhauVaBotInline(admin.TabularInline):
    model = DacDiemViPhauVaBot
    extra = 0

class TacDungVaCongDungInline(admin.TabularInline):
    model = TacDungVaCongDung
    extra = 0

class CheBienInline(admin.TabularInline):
    model = CheBien
    extra = 0

class HinhAnhMinhHoaInline(admin.TabularInline):
    model = HinhAnhMinhHoa
    extra = 0

@admin.register(DuocLieu)
class DuocLieuAdmin(admin.ModelAdmin):
    list_display =('id', 'ten_tieng_viet', 'ten_la_tinh', 'ho_thuc_vat', 'ngay_dang', 'nguoi_dang')
    inlines = [TenKhoaHocInline, DacDiemVaPhanBoInline, BoPhanDungInline, ThanhPhanHoaHocInline, TacDungVaCongDungInline, CheBienInline, ChePhamInline, ChuYInline, GhiChuInline, DacDiemViPhauVaBotInline, HinhAnhMinhHoaInline, HinhAnhBoSungInline]

    prepopulated_fields = {'slug': ('ten_la_tinh',)}

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'nguoi_dang', None) is None:
            obj.nguoi_dang = request.user.last_name + " " +request.user.first_name
        obj.save()
#--------------------------------------
from .models import  Level0, Level1, Level2, Level3, Level4, Level5, HinhAnhLv0, HinhAnhLv1, HinhAnhLv2, HinhAnhLv3, HinhAnhLv4, HinhAnhLv5

class Level1Inline(admin.TabularInline):
    model = Level1
    extra = 0
class Level2Inline(admin.TabularInline):
    model = Level2
    extra = 0

class Level3Inline(admin.TabularInline):
    model = Level3
    extra = 0

class Level4Inline(admin.TabularInline):
    model = Level4
    extra = 0

class Level5Inline(admin.TabularInline):
    model = Level5
    extra = 0
#--------------------------------------
class HinhAnhLv0Inline(admin.TabularInline):
    model = HinhAnhLv0
    extra = 0

class HinhAnhLv1Inline(admin.TabularInline):
    model = HinhAnhLv1
    extra = 0

class HinhAnhLv2Inline(admin.TabularInline):
    model = HinhAnhLv2
    extra = 0

class HinhAnhLv3Inline(admin.TabularInline):
    model = HinhAnhLv3
    extra = 0

class HinhAnhLv4Inline(admin.TabularInline):
    model = HinhAnhLv4
    extra = 0

class HinhAnhLv5Inline(admin.TabularInline):
    model = HinhAnhLv5
    extra = 0
#--------------------------------------

@admin.register(Level0)
class Level0Admin(admin.ModelAdmin):
    list_display =('tieu_de_chinh', 'nguoi_dang')
    inlines = [HinhAnhLv0Inline, Level1Inline]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'nguoi_dang', None) is None:
            obj.nguoi_dang = request.user.last_name + " " +request.user.first_name
        obj.save()
#--------------------------------------

@admin.register(Level1)
class Level1Admin(admin.ModelAdmin):
    list_display =('tieu_de_1','level_0')
    fields = [('tieu_de_1', 'level_0'), 'noi_dung']
    inlines = [HinhAnhLv1Inline, Level2Inline]
#--------------------------------------

@admin.register(Level2)
class Level1Admin(admin.ModelAdmin):
    list_display =('tieu_de_2','level_1')
    fields = [('tieu_de_2', 'level_1')]
    inlines = [HinhAnhLv2Inline, Level3Inline]
#--------------------------------------

@admin.register(Level3)
class Level3Admin(admin.ModelAdmin):
    list_display =('tieu_de_3','level_2')
    fields = [('tieu_de_3', 'level_2')]
    inlines = [HinhAnhLv3Inline, Level4Inline]
#--------------------------------------
@admin.register(Level4)
class Level3Admin(admin.ModelAdmin):
    list_display =('tieu_de_4','level_3')
    fields = [('tieu_de_4', 'level_3')]
    inlines = [HinhAnhLv4Inline, Level5Inline]
#--------------------------------------
@admin.register(Level5)
class Level3Admin(admin.ModelAdmin):
    list_display =('tieu_de_5','level_4')
    fields = [('tieu_de_5', 'level_4')]
    inlines = [HinhAnhLv5Inline]
#--------------------------------------
#--------------------------------------
