# Generated by Django 3.1.6 on 2021-03-27 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level0',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tieu_de_chinh', models.CharField(max_length=200, verbose_name='tiêu đề chính')),
                ('noi_dung', models.TextField(blank=True, max_length=2000, null=True, verbose_name='mục tiêu')),
                ('nguoi_dang', models.CharField(blank=True, help_text='Tên tác giả, nếu không nhập thông tin chương trình sẽ mặc định là họ và tên của chủ tài khoản (thông tin khai báo lúc đăng ký tài khoản / tạo bởi admin).', max_length=200, null=True, verbose_name='người đăng')),
                ('slug', models.SlugField(allow_unicode=True, help_text='Thông tin này sẽ hiển thị tại địa chỉ web, ví dụ: www.home/duoclieu/XXXXX, với XXXX là thông tin bạn nhập vào', null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Tiêu để chính',
                'verbose_name_plural': 'C. Tiêu để chính',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Level1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tieu_de_1', models.CharField(blank=True, max_length=200, null=True, verbose_name='tiêu đề cấp 1')),
                ('noi_dung', models.TextField(blank=True, max_length=2000, null=True, verbose_name='nội dung')),
                ('level_0', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kiem_nghiem.level0', verbose_name='<-- Level0')),
            ],
            options={
                'verbose_name': 'Tiêu đề cấp 1',
                'verbose_name_plural': 'C.1 - Tiêu đề cấp 1',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Level2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tieu_de_2', models.CharField(blank=True, max_length=200, null=True, verbose_name='tiêu đề cấp 2')),
                ('noi_dung', models.TextField(blank=True, max_length=2000, null=True, verbose_name='nội dung')),
                ('level_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kiem_nghiem.level1', verbose_name='<-- Tiêu đề cấp 1')),
            ],
            options={
                'verbose_name': 'Tiêu đề cấp 2',
                'verbose_name_plural': 'C.1.1 - Tiêu đề cấp 2',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Level3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tieu_de_3', models.CharField(blank=True, max_length=200, null=True, verbose_name='tiêu đề cấp 3')),
                ('noi_dung', models.TextField(blank=True, max_length=2000, null=True, verbose_name='nội dung')),
                ('level_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kiem_nghiem.level2', verbose_name='<-- Tiêu đề cấp 2')),
            ],
            options={
                'verbose_name': 'Tiêu đề cấp 3',
                'verbose_name_plural': 'C.1.1.1 - Tiêu đề cấp 3',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Level4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tieu_de_4', models.CharField(blank=True, max_length=200, null=True, verbose_name='tiêu đề cấp 4')),
                ('noi_dung', models.TextField(blank=True, max_length=2000, null=True, verbose_name='nội dung')),
                ('level_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kiem_nghiem.level3', verbose_name='<-- Tiêu đề cấp 3')),
            ],
            options={
                'verbose_name': 'Tiêu đề cấp 4',
                'verbose_name_plural': 'C.1.1.1.1 - Tiêu đề cấp 4',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Level5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tieu_de_5', models.CharField(blank=True, max_length=200, null=True, verbose_name='tiêu đề cấp 5')),
                ('noi_dung', models.TextField(blank=True, max_length=2000, null=True, verbose_name='nội dung')),
                ('level_4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kiem_nghiem.level4', verbose_name='<-- Tiêu đề cấp 4')),
            ],
            options={
                'verbose_name': 'Tiêu đề cấp 5',
                'verbose_name_plural': 'C.1.1.1.1.1 - Tiêu đề cấp 5',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='HinhAnhLv5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hinh', models.ImageField(upload_to='giaotrinh')),
                ('ten_hinh', models.CharField(max_length=200)),
                ('level_5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kiem_nghiem.level5')),
            ],
        ),
        migrations.CreateModel(
            name='HinhAnhLv4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hinh', models.ImageField(upload_to='giaotrinh')),
                ('ten_hinh', models.CharField(max_length=200)),
                ('level_4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kiem_nghiem.level4')),
            ],
        ),
        migrations.CreateModel(
            name='HinhAnhLv3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hinh', models.ImageField(upload_to='giaotrinh')),
                ('ten_hinh', models.CharField(max_length=200)),
                ('level_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kiem_nghiem.level3')),
            ],
        ),
        migrations.CreateModel(
            name='HinhAnhLv2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hinh', models.ImageField(upload_to='giaotrinh')),
                ('ten_hinh', models.CharField(max_length=200)),
                ('level_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kiem_nghiem.level2')),
            ],
        ),
        migrations.CreateModel(
            name='HinhAnhLv1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hinh', models.ImageField(upload_to='giaotrinh')),
                ('ten_hinh', models.CharField(max_length=200)),
                ('level_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kiem_nghiem.level1')),
            ],
        ),
        migrations.CreateModel(
            name='HinhAnhLv0',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hinh', models.ImageField(upload_to='giaotrinh')),
                ('ten_hinh', models.CharField(max_length=200)),
                ('level_0', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kiem_nghiem.level0')),
            ],
        ),
    ]
