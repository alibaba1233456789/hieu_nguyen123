from django.db import models
from django.urls import reverse
from datetime import date, datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
#------------------------------------------------------------------
class LoiNoiDau(models.Model):
    su_menh = models.TextField(max_length = 1000, verbose_name = 'Sứ mệnh', null = True, blank = True, help_text = 'Mỗi "+Add" là một đoạn trong "Sứ mệnh".')
    xay_dung = models.TextField(max_length = 1000, verbose_name = 'Cách thức xây dựng thông tin', null = True, blank = True, help_text = 'Mỗi "+Add" là một đoạn trong "Cách thức xây dựng thông tin".')
    phan_quyen = models.TextField(max_length = 1000, verbose_name = 'Phân quyền', null = True, blank = True, help_text = 'Mỗi "+Add" là một đoạn trong "Phân quyền".')
    tra_cuu = models.TextField(max_length = 1000, verbose_name = 'Cách thức tra cứu', null = True, blank = True, help_text = 'Mỗi "+Add" là một đoạn trong "Cách thức tra cứu".')

    class Meta:
       verbose_name = 'Lời nói đầu'
       verbose_name_plural = '0. Lời nói đầu'
       ordering = ['id']

    def __str__(self):
        return f'Lời nói đầu {self.id}'
