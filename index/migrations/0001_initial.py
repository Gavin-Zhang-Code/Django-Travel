# Generated by Django 2.1.8 on 2019-08-30 05:44

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='home_information',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.IntegerField(unique=True)),
                ('home', models.CharField(max_length=20)),
                ('person', models.IntegerField()),
                ('clean', models.IntegerField()),
            ],
            options={
                'verbose_name': '房间信息',
                'db_table': 'home_infor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='information',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('home', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('num', models.IntegerField()),
                ('detail', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': '酒店信息',
                'db_table': 'hotel_infor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.IntegerField(unique=True)),
                ('pay', models.IntegerField()),
                ('auto_time', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '订单信息',
                'db_table': 'order',
                'managed': False,
            },
        ),
    ]
