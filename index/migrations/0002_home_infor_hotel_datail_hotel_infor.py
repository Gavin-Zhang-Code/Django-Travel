# Generated by Django 2.1.8 on 2019-08-30 06:21

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='home_infor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.IntegerField(unique=True, verbose_name='房号')),
                ('home', models.CharField(max_length=20, verbose_name='房间类型')),
                ('person_num', models.IntegerField(verbose_name='容纳人数')),
                ('person', models.IntegerField(verbose_name='是否入住，1为入住')),
                ('clean', models.IntegerField(verbose_name='是否打扫，1为已打扫')),
            ],
            options={
                'verbose_name': '房间信息',
                'db_table': 'home_infor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='hotel_datail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='酒店名称')),
                ('min_price', models.IntegerField(verbose_name='最低价')),
                ('max_price', models.IntegerField(verbose_name='最高价')),
                ('detail', ckeditor.fields.RichTextField(verbose_name='酒店介绍')),
                ('address', models.CharField(max_length=100, verbose_name='地址')),
                ('phone', models.IntegerField(verbose_name='联系电话')),
            ],
            options={
                'verbose_name': '酒店详情',
                'db_table': 'hotel_detail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='hotel_infor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('home', models.CharField(max_length=20, verbose_name='房间类型')),
                ('price', models.IntegerField(verbose_name='价格')),
                ('num', models.IntegerField(verbose_name='剩余数量')),
                ('detail', ckeditor.fields.RichTextField(verbose_name='房屋详情')),
            ],
            options={
                'verbose_name': '酒店房间信息',
                'db_table': 'hotel_infor',
                'managed': False,
            },
        ),
    ]
