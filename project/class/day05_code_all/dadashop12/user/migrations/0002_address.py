# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-04-13 08:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.CharField(max_length=11, verbose_name='收件人名')),
                ('address', models.CharField(max_length=100, verbose_name='用户地址')),
                ('is_default', models.BooleanField(default=False, verbose_name='是否为默认地址')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否活跃')),
                ('postcode', models.CharField(max_length=7, verbose_name='邮编')),
                ('receiver_mobile', models.CharField(max_length=11, verbose_name='收件人电话')),
                ('tag', models.CharField(max_length=10, verbose_name='标签')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserProfile')),
            ],
        ),
    ]
