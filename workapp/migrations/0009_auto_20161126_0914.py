# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-26 09:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0008_auto_20161126_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collect',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 26, 9, 14, 50, 271920)),
        ),
        migrations.AlterField(
            model_name='houseinfo',
            name='housetype',
            field=models.CharField(choices=[('三室一厅一卫', '三室一厅一卫'), ('三室两厅两卫', '三室两厅两卫'), ('三室一厅两卫', '三室一厅两卫'), ('四室两厅两卫', '四室两厅两卫'), ('二室一厅一卫', '二室一厅一卫'), ('一室一厅一卫', '一室一厅一卫')], max_length=200),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='sex',
            field=models.CharField(choices=[('男', '男'), ('女', '女'), ('保密', '保密')], default='保密', max_length=10),
        ),
    ]
