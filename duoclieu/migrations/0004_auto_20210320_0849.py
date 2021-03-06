# Generated by Django 3.1.6 on 2021-03-20 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('duoclieu', '0003_auto_20210320_0825'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='level1',
            options={'ordering': ['id'], 'verbose_name': 'Tiêu đề cấp 1', 'verbose_name_plural': 'C.1 - Tiêu đề cấp 1'},
        ),
        migrations.AlterModelOptions(
            name='level2',
            options={'ordering': ['id'], 'verbose_name': 'Tiêu đề cấp 2', 'verbose_name_plural': 'C.1.1 - Tiêu đề cấp 2'},
        ),
        migrations.AlterModelOptions(
            name='level3',
            options={'ordering': ['id'], 'verbose_name': 'Tiêu đề cấp 3', 'verbose_name_plural': 'C.1.1.1 - Tiêu đề cấp 3'},
        ),
        migrations.AlterModelOptions(
            name='level4',
            options={'ordering': ['id'], 'verbose_name': 'Tiêu đề cấp 4', 'verbose_name_plural': 'C.1.1.1.1 - Tiêu đề cấp 4'},
        ),
        migrations.AlterModelOptions(
            name='level5',
            options={'ordering': ['id'], 'verbose_name': 'Tiêu đề cấp 5', 'verbose_name_plural': 'C.1.1.1.1.1 - Tiêu đề cấp 5'},
        ),
        migrations.AlterModelOptions(
            name='nhomhoatchat',
            options={'ordering': ['id'], 'verbose_name': 'Nhóm hoạt chất', 'verbose_name_plural': 'C. Nhóm hoạt chất'},
        ),
        migrations.AlterField(
            model_name='hothucvat',
            name='slug',
            field=models.SlugField(help_text='Thông tin này sẽ hiển thị tại địa chỉ web, ví dụ: www.home/duoclieu/XXXXX, nếu không nhập dữ liệu chương trình sẽ mặc định XXXXX là tên khoa học của dược liệu.', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='level2',
            name='level_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='duoclieu.level1', verbose_name='<-- Tiêu đề cấp 1'),
        ),
        migrations.AlterField(
            model_name='level3',
            name='level_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='duoclieu.level2', verbose_name='<-- Tiêu đề cấp 2'),
        ),
        migrations.AlterField(
            model_name='level4',
            name='level_3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='duoclieu.level3', verbose_name='<-- Tiêu đề cấp 3'),
        ),
        migrations.AlterField(
            model_name='level5',
            name='level_4',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='duoclieu.level4', verbose_name='<-- Tiêu đề cấp 4'),
        ),
        migrations.AlterField(
            model_name='nhomhoatchat',
            name='slug',
            field=models.SlugField(allow_unicode=True, help_text='Thông tin này sẽ hiển thị tại địa chỉ web, ví dụ: www.home/duoclieu/XXXXX, nếu không nhập dữ liệu chương trình sẽ mặc định XXXXX là tên của nhóm hoạt chất.', null=True, unique=True),
        ),
    ]
