# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-07 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=40)),
                ('uemail', models.CharField(max_length=30)),
                ('ushou', models.CharField(default='', max_length=10)),
                ('uaddress', models.CharField(default='', max_length=100)),
                ('zipCode', models.CharField(default='', max_length=6)),
                ('phone', models.CharField(default='', max_length=11)),
            ],
        ),
    ]
